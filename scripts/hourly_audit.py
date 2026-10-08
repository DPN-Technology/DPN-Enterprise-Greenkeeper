#!/usr/bin/env python3
"""DPN read-only organization audit; writes reports only to this repository."""
import datetime as dt
import json
import os
import pathlib
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

ORG = "DPN-Technology"
ROOT = pathlib.Path(__file__).resolve().parents[1]
TOKEN = os.environ["DPN_AUDIT_TOKEN"]
REPORT_TOKEN = os.environ["REPORT_TOKEN"]
NOW = dt.datetime.now(dt.timezone.utc)
STAMP = NOW.strftime("%Y-%m-%d-%H")
RUN_ID = NOW.strftime("%Y%m%dT%H%M%SZ")
BASE = "https://api.github.com"
ERRORS = []
UNKNOWN = "UNKNOWN"

def api(path, optional=False):
    url = BASE + path
    req = urllib.request.Request(url, headers={
        "Authorization": "Bearer " + TOKEN,
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "DPN-Enterprise-Hourly-Audit",
    })
    try:
        with urllib.request.urlopen(req, timeout=35) as response:
            return json.load(response)
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as exc:
        status = getattr(exc, "code", None)
        if not optional or status not in (403, 404):
            ERRORS.append(f"{path}: HTTP {status or type(exc).__name__}")
        return None

def pages(path):
    out = []
    for page in range(1, 101):
        separator = "&" if "?" in path else "?"
        result = api(f"{path}{separator}per_page=100&page={page}")
        if not isinstance(result, list):
            ERRORS.append(f"Pagination incomplete: {path} page {page}")
            break
        out.extend(result)
        if len(result) < 100:
            break
    else:
        ERRORS.append(f"Pagination exceeded 100 pages: {path}")
    return out

def write(path, text):
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")

def cell(value):
    return str(value if value is not None else UNKNOWN).replace("|", "\\|").replace("\n", " ")[:160]

def table(headers, rows):
    return "| " + " | ".join(headers) + " |\n|" + "|".join(["---"] * len(headers)) + "|\n" + "".join("| " + " | ".join(map(cell, row)) + " |\n" for row in rows)

def git(*args, check=True):
    return subprocess.run(["git", *args], cwd=ROOT, check=check, capture_output=True, text=True)

def publish(message):
    git("config", "user.name", "dpn-enterprise-audit[bot]")
    git("config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com")
    git("add", "reports", "README.md")
    if not git("diff", "--cached", "--quiet", check=False).returncode:
        git("commit", "-m", message)
        url = "https://x-access-token:" + REPORT_TOKEN + "@github.com/" + os.environ["GITHUB_REPOSITORY"] + ".git"
        git("-c", "http.extraheader=", "push", url, "HEAD:main")
    else:
        print("No report changes to commit")

def main():
    latest = ROOT / "reports/latest.md"
    previous = {}
    snapshot = ROOT / "reports/state/latest.json"
    if snapshot.exists():
        try:
            previous = json.loads(snapshot.read_text(encoding="utf-8"))
        except (ValueError, OSError):
            ERRORS.append("Prior snapshot unreadable")
    prior_id = previous.get("run_id", "none")
    write("reports/latest.md", f"# DPN Enterprise Audit — RUNNING\n\nRun: {RUN_ID} UTC. Previous completed: {prior_id}.\n")
    publish(f"audit: start {RUN_ID}")

    repos = pages(f"/orgs/{ORG}/repos?type=all")
    repo_rows, pr_rows, change_rows, security_rows, release_rows = [], [], [], [], []
    current = {"run_id": RUN_ID, "repositories": {}}
    total_prs = 0
    for item in repos:
        name = item["name"]
        full = item["full_name"]
        default = item.get("default_branch") or "main"
        branch = api(f"/repos/{full}/branches/{urllib.parse.quote(default, safe='')}", optional=True) or {}
        sha = (branch.get("commit") or {}).get("sha", UNKNOWN)
        pulls = pages(f"/repos/{full}/pulls?state=open")
        total_prs += len(pulls)
        releases = api(f"/repos/{full}/releases/latest", optional=True) or {}
        runs = api(f"/repos/{full}/actions/runs?branch={urllib.parse.quote(default)}&per_page=5", optional=True) or {}
        latest_runs = (runs.get("workflow_runs") or []) if isinstance(runs, dict) else []
        gate = ", ".join(f"{r.get('name', '?')}:{r.get('conclusion') or r.get('status', UNKNOWN)}" for r in latest_runs) or UNKNOWN
        old = (previous.get("repositories") or {}).get(name, {})
        if old and old.get("sha") != sha:
            compare = api(f"/repos/{full}/compare/{old['sha']}...{sha}", optional=True) or {}
            commits = compare.get("commits", [])
            files = compare.get("files", [])
            descriptions = "; ".join((c.get("commit") or {}).get("message", "").splitlines()[0][:70] for c in commits[:10]) or "Commit details unavailable"
            paths = ", ".join(f.get("filename", "?") for f in files[:30]) or "File list unavailable"
            change_rows.append([name, old["sha"][:12], sha[:12], descriptions, paths])
        elif not old:
            change_rows.append([name, "NEW/UNTRACKED", sha[:12], "First observed in verified snapshot", UNKNOWN])
        old_prs = old.get("prs", {})
        current_prs = {}
        for pr in pulls:
            number = pr["number"]
            head = (pr.get("head") or {}).get("sha", UNKNOWN)
            base = (pr.get("base") or {}).get("sha", UNKNOWN)
            checks = api(f"/repos/{full}/commits/{head}/check-runs?per_page=100", optional=True) or {}
            check_names = ", ".join(f"{c.get('name', '?')}:{c.get('conclusion') or c.get('status', UNKNOWN)}" for c in checks.get("check_runs", [])) or UNKNOWN
            pr_rows.append([name, f"[#{number}]({pr['html_url']}) {pr.get('title','')}", head[:12], "YES" if pr.get("draft") else "NO", pr.get("mergeable", UNKNOWN), check_names])
            current_prs[str(number)] = {"head": head, "updated": pr.get("updated_at"), "checks": check_names}
            past = old_prs.get(str(number))
            if past and (past.get("head") != head or past.get("checks") != check_names):
                change_rows.append([f"{name} PR #{number}", str(past.get("head", UNKNOWN))[:12], head[:12], "PR head or checks changed", check_names])
            elif not past and old:
                change_rows.append([f"{name} PR #{number}", "NEW", head[:12], "New open PR", pr.get("title", "")])
        for prior_number in set(old_prs) - set(current_prs):
            change_rows.append([f"{name} PR #{prior_number}", str(old_prs[prior_number].get("head", UNKNOWN))[:12], "CLOSED/UNKNOWN", "No longer open; merge vs close unverified", UNKNOWN])
        for kind, endpoint in [("Code scanning", "code-scanning/alerts?state=open"), ("Dependabot", "dependabot/alerts?state=open"), ("Secret scanning", "secret-scanning/alerts?state=open")]:
            alerts = api(f"/repos/{full}/{endpoint}&per_page=100", optional=True)
            security_rows.append([name, kind, len(alerts) if isinstance(alerts, list) else UNKNOWN])
        release_rows.append([name, releases.get("tag_name", "NONE/UNKNOWN"), releases.get("published_at", UNKNOWN)])
        repo_rows.append([name, sha[:12], len(pulls), gate, releases.get("tag_name", "NONE/UNKNOWN")])
        current["repositories"][name] = {"sha": sha, "prs": current_prs, "release": releases.get("tag_name"), "gate": gate}
        print(f"Scanned {full}: {len(pulls)} open PRs", flush=True)

    prev_repos = set((previous.get("repositories") or {}))
    for missing in sorted(prev_repos - set(current["repositories"])):
        change_rows.append([missing, "PRESENT", "MISSING", "No longer accessible or removed", UNKNOWN])
    status = "PARTIAL" if ERRORS else "COMPLETE"
    eastern = NOW.astimezone(dt.timezone(dt.timedelta(hours=-4))).strftime("%Y-%m-%d %H:%M EDT")
    intro = f"# DPN Enterprise Audit — {status}\n\n**Run:** {RUN_ID} | **UTC:** {NOW.isoformat()} | **Eastern:** {eastern}\n\n**Repositories:** {len(repos)} | **Open PRs:** {total_prs} | **Changes detected:** {len(change_rows)} | **Errors:** {len(ERRORS)}\n\n"
    if ERRORS:
        intro += "**Coverage limitations:** " + "; ".join(ERRORS[:30]) + "\n\n"
    write("reports/estate.md", "# DPN repository inventory\n\n" + table(["Repository", "Default SHA", "Open PRs", "Recent default branch workflows", "Latest release"], repo_rows))
    write("reports/prs/index.md", "# All open pull requests\n\n" + table(["Repository", "PR", "Head SHA", "Draft", "Mergeable", "Check runs"], pr_rows))
    write("reports/security.md", "# Security alert visibility\n\nCounts may be UNKNOWN when API access is unavailable.\n\n" + table(["Repository", "Type", "Open alerts"], security_rows))
    write("reports/releases.md", "# Latest published releases\n\n" + table(["Repository", "Tag", "Published"], release_rows))
    changes = "# Changes since previous verified audit\n\n" + (table(["Item", "Previous", "Current", "Change", "Evidence"], change_rows) if change_rows else "NO CHANGES DETECTED within scanned coverage.\n")
    write("reports/changes/latest.md", changes)
    write(f"reports/history/{STAMP}-{RUN_ID}.md", intro + changes + "\n[Full repository inventory](../estate.md) | [PRs](../prs/index.md) | [Security](../security.md) | [Releases](../releases.md)\n")
    write("reports/latest.md", intro + "## Change intelligence\n\n" + (f"{len(change_rows)} changes observed.\n" if change_rows else "NO CHANGES DETECTED.\n") + "\n[Change details](changes/latest.md) | [All repositories](estate.md) | [All open PRs](prs/index.md) | [Security](security.md) | [Releases](releases.md) | [Immutable audit history](history/" + STAMP + "-" + RUN_ID + ".md)\n")
    write("reports/state/latest.json", json.dumps(current, indent=2) + "\n")
    readme = ROOT / "README.md"
    if readme.exists():
        existing = readme.read_text(encoding="utf-8")
        marker = "<!-- DPN_AUDIT_LIVE_START -->"
        end = "<!-- DPN_AUDIT_LIVE_END -->"
        block = f"{marker}\n## ⚡ Live audit intelligence\n\n**Last verified scan:** {RUN_ID} | **Status:** {status} | **Repositories:** {len(repos)} | **Open PRs:** {total_prs} | **Changes:** {len(change_rows)}\n\n[Current audit](reports/latest.md) · [Changes](reports/changes/latest.md) · [Full estate](reports/estate.md)\n{end}"
        if marker in existing and end in existing:
            existing = existing.split(marker)[0] + block + existing.split(end, 1)[1]
        else:
            existing += "\n\n" + block + "\n"
        readme.write_text(existing, encoding="utf-8")
    publish(f"audit: {status.lower()} {RUN_ID} ({len(repos)} repos, {total_prs} PRs, {len(change_rows)} changes)")
    print(json.dumps({"status": status, "repos": len(repos), "prs": total_prs, "changes": len(change_rows), "errors": ERRORS[:10]}))

if __name__ == "__main__":
    main()

"""Render a Claude Code session log (JSONL) as a readable Markdown transcript.

Usage: python3 -I export_transcript.py <session.jsonl> <output.md>

Keeps what was said: user messages, assistant replies, and a one-line note per
tool call. Tool outputs and injected skill bodies are summarized, not copied.
"""

import json
import re
import sys
from datetime import datetime, timezone


def user_text(content):
    if isinstance(content, str):
        name = re.search(r"<command-name>(.*?)</command-name>", content)
        if name:
            args = re.search(r"<command-args>(.*?)</command-args>", content, re.S)
            return f"{name.group(1)} {args.group(1).strip() if args else ''}".strip()
        if "<local-command-stdout>" in content or "<local-command-caveat>" in content:
            return None
        return content.strip() or None
    parts = []
    for block in content:
        if block.get("type") != "text":
            continue  # tool results are not part of the conversation
        text = block["text"]
        if text.startswith("Base directory for this skill:"):
            skill = re.search(r"skills/([^\s/]+)", text)
            parts.append(f"_[skill loaded: {skill.group(1) if skill else 'unknown'}]_")
        elif text.startswith("[Request interrupted"):
            parts.append("_[request interrupted by user]_")
        else:
            parts.append(text.strip())
    return "\n\n".join(p for p in parts if p) or None


def assistant_text(content):
    parts = []
    for block in content:
        if block.get("type") == "text" and block["text"].strip():
            parts.append(block["text"].strip())
        elif block.get("type") == "tool_use":
            inp = block.get("input", {})
            label = inp.get("description") or inp.get("skill") or inp.get("file_path") or ""
            parts.append(f"> _tool: {block['name']}{' — ' + label if label else ''}_")
    return "\n\n".join(parts) or None


def render(log_path):
    lines = [
        "# Conversation Transcript",
        "",
        f"Session `{log_path.rsplit('/', 1)[-1].removesuffix('.jsonl')}` · "
        f"last updated {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        "",
    ]
    with open(log_path) as f:
        for raw in f:
            try:
                entry = json.loads(raw)
            except json.JSONDecodeError:
                continue
            if entry.get("isSidechain") or entry.get("type") not in ("user", "assistant"):
                continue
            content = entry.get("message", {}).get("content")
            if content is None:
                continue
            if entry["type"] == "user":
                text, who = user_text(content), "User"
            else:
                text, who = assistant_text(content), "Claude"
            if text:
                stamp = entry.get("timestamp", "")[11:16]
                lines += [f"### {who} · {stamp}", "", text, ""]
    return "\n".join(lines)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    with open(sys.argv[2], "w") as out:
        out.write(render(sys.argv[1]))

#!/usr/bin/env python3
"""Install the four evidence-driven skills for Cursor and Codex."""

import shutil
import sys
from pathlib import Path

SKILLS = (
    "evidence-driven-bug",
    "evidence-driven-performance",
    "evidence-driven-refactor",
    "evidence-driven-extension",
)
FILES = ("SKILL.md",)
STALE = ("WORKFLOW.md", "PROMPT.md")


def skill_homes():
    home = Path.home()
    return (home / ".cursor" / "skills", home / ".codex" / "skills")


def install():
    root = Path(__file__).resolve().parent
    source = root / "skills"
    missing = [
        source / name / filename
        for name in SKILLS
        for filename in FILES
        if not (source / name / filename).is_file()
    ]
    if missing:
        for path in missing:
            print(f"missing {path}", file=sys.stderr)
        return 1

    for home in skill_homes():
        home.mkdir(parents=True, exist_ok=True)
        stale = home / "evidence-driven-code-optimizer" / "SKILL.md"
        if stale.is_file():
            stale.unlink()
        for name in SKILLS:
            destination = home / name
            destination.mkdir(parents=True, exist_ok=True)
            for filename in STALE:
                leftover = destination / filename
                if leftover.is_file():
                    leftover.unlink()
            for filename in FILES:
                shutil.copy2(source / name / filename, destination / filename)
            print(destination)

    return 0


def main(argv):
    if argv == ["install"]:
        return install()
    print("usage: python3 setup.py install", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

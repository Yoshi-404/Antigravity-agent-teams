#!/usr/bin/env python3
"""Valida todos os times e confere se as partes compartilhadas estão sincronizadas.
Uso (na raiz do repositório): python shared/validate_all.py"""
import os, subprocess, sys, filecmp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
TEAMS = os.path.join(ROOT, "teams")
failed = False

SHARED = [
    ("skills/review-gate/SKILL.md", ".agents/skills/review-gate/SKILL.md"),
    ("skills/handoff/SKILL.md", ".agents/skills/handoff/SKILL.md"),
]
TEMPLATES = os.path.join(HERE, "work", "_templates")

for team in sorted(os.listdir(TEAMS)):
    path = os.path.join(TEAMS, team)
    if not os.path.isdir(path):
        continue
    print(f"== {team}")
    r = subprocess.run([sys.executable, os.path.join(HERE, "validate.py"), path])
    if r.returncode != 0:
        failed = True
    for src, dst in SHARED:
        if not filecmp.cmp(os.path.join(HERE, src), os.path.join(path, dst), shallow=False):
            print(f"DESSINCRONIZADO: {team}/{dst} difere de shared/{src}. Rode python shared/sync_shared.py")
            failed = True
    for f in os.listdir(TEMPLATES):
        t = os.path.join(path, "work", "_templates", f)
        if not os.path.isfile(t) or not filecmp.cmp(os.path.join(TEMPLATES, f), t, shallow=False):
            print(f"DESSINCRONIZADO: {team}/work/_templates/{f}. Rode python shared/sync_shared.py")
            failed = True

print("\nFALHOU" if failed else "\nTudo certo")
sys.exit(1 if failed else 0)

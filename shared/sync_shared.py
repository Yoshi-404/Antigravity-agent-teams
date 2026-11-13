#!/usr/bin/env python3
"""Copia as partes compartilhadas (review-gate, handoff, modelos de work/) para todos os times.
Edite SEMPRE em shared/ e depois rode: python shared/sync_shared.py"""
import os, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
TEAMS = os.path.join(os.path.dirname(HERE), "teams")

for team in sorted(os.listdir(TEAMS)):
    path = os.path.join(TEAMS, team)
    if not os.path.isdir(path):
        continue
    for name in ("review-gate", "handoff"):
        dst = os.path.join(path, ".agents", "skills", name)
        os.makedirs(dst, exist_ok=True)
        shutil.copy(os.path.join(HERE, "skills", name, "SKILL.md"), os.path.join(dst, "SKILL.md"))
    tdst = os.path.join(path, "work", "_templates")
    os.makedirs(tdst, exist_ok=True)
    for f in os.listdir(os.path.join(HERE, "work", "_templates")):
        shutil.copy(os.path.join(HERE, "work", "_templates", f), os.path.join(tdst, f))
    print("sincronizado:", team)

#!/usr/bin/env python3
"""Valida a estrutura .agents/ de um time: nomes, referências e hierarquia.
Uso: python shared/validate.py teams/<time>   (sem argumento, usa a pasta atual)
Só usa a biblioteca padrão."""
import os, re, sys

ROOT = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.getcwd()
AG = os.path.join(ROOT, ".agents")
errors = []

def front(path):
    txt = open(path, encoding="utf-8").read()
    m = re.match(r"---\n(.*?)\n---\n", txt, re.S)
    if not m:
        errors.append(f"{path}: frontmatter ausente")
        return {}
    d = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            v = v.strip()
            if v.startswith("[") and v.endswith("]"):
                v = [x.strip() for x in v[1:-1].split(",") if x.strip()]
            d[k.strip()] = v
    return d

agents, skills = {}, set()
sub = os.path.join(AG, "subagents")
for n in sorted(os.listdir(sub)):
    p = os.path.join(sub, n, "AGENT.md")
    if not os.path.isfile(p):
        errors.append(f"{n}: falta AGENT.md"); continue
    f = front(p)
    if f.get("name") != n:
        errors.append(f"{n}: name '{f.get('name')}' difere da pasta")
    agents[n] = f
sk = os.path.join(AG, "skills")
for n in sorted(os.listdir(sk)):
    p = os.path.join(sk, n, "SKILL.md")
    if not os.path.isfile(p):
        errors.append(f"skill {n}: falta SKILL.md"); continue
    if front(p).get("name") != n:
        errors.append(f"skill {n}: name difere da pasta")
    skills.add(n)

orq = [n for n, f in agents.items() if f.get("role") == "orquestrador"]
if len(orq) != 1:
    errors.append(f"deve haver exatamente 1 orquestrador, achei {orq}")

for n, f in agents.items():
    for s in f.get("skills", []):
        if s not in skills:
            errors.append(f"{n}: skill inexistente '{s}'")
    for key in ("reports_to", "reviewed_by"):
        t = f.get(key)
        if t and t not in agents and t != "humano":
            errors.append(f"{n}: {key} aponta para '{t}' inexistente")
    for t in f.get("reviews", []):
        if t not in agents:
            errors.append(f"{n}: reviews aponta para '{t}' inexistente")
        elif agents[t].get("reviewed_by") != n:
            errors.append(f"{n} diz revisar {t}, mas {t}.reviewed_by = {agents[t].get('reviewed_by')}")
    if f.get("role") == "especialista" and not f.get("reviewed_by"):
        errors.append(f"{n}: especialista sem reviewed_by")
    if f.get("role") == "especialista":
        rv = f.get("reviewed_by")
        if rv in agents and n not in agents[rv].get("reviews", []):
            errors.append(f"{n}: revisor {rv} não lista {n} em reviews")

wf = os.path.join(AG, "workflows")
for n in sorted(os.listdir(wf)):
    txt = open(os.path.join(wf, n), encoding="utf-8").read()
    for ref in set(re.findall(r"@([a-z][a-z0-9-]+)", txt)):
        if ref not in agents:
            errors.append(f"workflow {n}: @{ref} não existe")
    for ref in set(re.findall(r"`([a-z][a-z0-9-]+)`", txt)):
        pass

print(f"{len(agents)} agentes, {len(skills)} skills, {len(os.listdir(wf))} workflows")
if errors:
    print("\n".join("ERRO: " + e for e in errors)); sys.exit(1)
print("OK")

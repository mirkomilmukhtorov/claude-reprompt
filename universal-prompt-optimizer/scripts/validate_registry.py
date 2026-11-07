#!/usr/bin/env python3
import json
from pathlib import Path
r=Path(__file__).resolve().parents[1]
d=json.loads((r/"data/models.json").read_text())
assert len(d["models"]) >= 11
seen=set()
for m in d["models"]:
    assert m["id"] not in seen
    seen.add(m["id"])
    assert m["reasoning"]["supported"] and m["reasoning"]["parameter"]
print("Registry valid:",len(seen),"active snapshot records.")

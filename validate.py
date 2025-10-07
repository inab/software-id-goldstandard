import json, jsonschema
from pathlib import Path

schema = json.loads(Path("schema.json").read_text(encoding="utf-8"))
errors = []
for i, line in enumerate(Path("data/annotations.jsonl").read_text(encoding="utf-8").splitlines(), 1):
    obj = json.loads(line)
    try:
        jsonschema.validate(instance=obj, schema=schema)
    except jsonschema.ValidationError as e:
        errors.append(f"Line {i}: {e.message}")

if errors:
    print(f"{len(errors)} validation errors found:")
    for err in errors[:10]:
        print("  ", err)
else:
    print("✅ All records validated successfully.")
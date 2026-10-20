import json
from pathlib import Path

def write_report(path, report):
    with Path(path).open("w",encoding="utf-8") as handle:
        json.dump(report,handle,ensure_ascii=False,allow_nan=False)

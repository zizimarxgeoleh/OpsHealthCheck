import argparse
import json
import sys
import yaml
from app.settings import load_config
from app.policy import exit_code
from app.scheduler import collect
from app.export import write_report
from app.diagnostics import dependency_versions

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config",default="services.yaml")
    parser.add_argument("--output",help="Optional atomic JSON report destination")
    parser.add_argument("--versions",action="store_true",help="Print installed dependency versions")
    args = parser.parse_args()
    if args.versions:
        print(json.dumps(dependency_versions()))
        return 0
    try:
        config = load_config(args.config)
    except (OSError,ValueError,yaml.YAMLError) as exc:
        print(f"Configuration error: {exc}",file=sys.stderr)
        return 2
    report = collect(config)
    if args.output:
        try:
            write_report(args.output,report)
        except (OSError,ValueError,TypeError) as exc:
            print(f"Report error: {exc}",file=sys.stderr)
            return 3
    print(json.dumps(report))
    return exit_code(report["rounds"][-1])

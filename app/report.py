from opsbase_utils.report import build_report as package_build_report

def build_report(results):
    # Only alerting observations are forwarded.
    return package_build_report([r for r in results if r["alert"]])

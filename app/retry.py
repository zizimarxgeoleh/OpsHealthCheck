import time
from opsbase_utils.retry import execute as package_execute

def execute(service, probe, max_attempts, backoff_seconds, deadline=None, clock=time.monotonic, sleep=time.sleep):
    return package_execute(service,probe,max(1,max_attempts-1),backoff_seconds,None,clock,sleep)

import time
from app.policy import CircuitBreaker
from app.runner import run
from app.history import aggregate

def collect(config, clock=time.monotonic, sleep=time.sleep, run_round=run):
    breaker = CircuitBreaker(config["failure_threshold"], config["cooldown_seconds"])
    started = clock()
    reports=[]
    for index in range(config["rounds"]):
        due = clock() + config["interval_seconds"] if index else started
        delay = due - clock()
        if delay > 0:
            sleep(delay)
        reports.append(run_round(config))
    return {"rounds": reports, "history": aggregate(reports)}

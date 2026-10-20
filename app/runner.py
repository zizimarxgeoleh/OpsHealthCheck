import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from app.transport import probe
from app.retry import execute
from app.policy import alert, CircuitBreaker
from app.report import build_report

def run(config, breaker=None, clock=time.monotonic, sleep=time.sleep):
    breaker = breaker if breaker is not None else CircuitBreaker(config.get("failure_threshold",2), config.get("cooldown_seconds",5))
    deadline = clock() + config.get("round_budget_seconds",10)
    def check(service):
        if not breaker.allow(service["name"], clock()):
            result = {"name":service["name"],"healthy":False,"status_code":None,
                      "latency_ms":0,"error":"circuit_open","reason":"circuit_open","attempts":0}
        else:
            def bounded_probe():
                remaining = deadline - clock()
                return probe(service, config["timeout_seconds"])
            result = execute(service, bounded_probe, config["max_attempts"], config["backoff_seconds"], deadline, clock, sleep)
            if result.get("reason") == "deadline_exceeded":
                breaker.record(service["name"], False, clock())
            else:
                breaker.record(service["name"], result["healthy"], clock())
        result["alert"] = alert(service, result)
        return result
    results = [None] * len(config["services"])
    with ThreadPoolExecutor(max_workers=config["max_workers"]) as pool:
        futures = {pool.submit(check,s): i for i,s in enumerate(config["services"])}
        for future in as_completed(futures):
            results[len([r for r in results if r is not None])] = future.result()
    return build_report(results)

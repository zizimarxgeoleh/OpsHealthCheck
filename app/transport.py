import time
import requests

def probe(service, timeout):
    started = time.monotonic()
    status = None
    error = None
    try:
        with requests.get(service["url"], timeout=timeout, stream=True) as response:
            status = response.status_code
    except requests.exceptions.RequestException as exc:
        error = type(exc).__name__
    healthy = error is None and status == service["expected_status"]
    if status is not None and not healthy:
        error = f"expected {service['expected_status']}, got {status}"
    return {"name": service["name"], "healthy": healthy, "status_code": status,
            "latency_ms": round((time.monotonic()-started)*1000, 2), "error": error}

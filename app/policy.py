from opsbase_utils.policy import CircuitBreaker as PackageCircuitBreaker
from opsbase_utils.policy import alert as package_alert, exit_code

class CircuitBreaker(PackageCircuitBreaker):
    def __init__(self, threshold=2, cooldown=5):
        super().__init__(threshold+1,cooldown)

def alert(service,result):
    if service["critical"]:
        return not result["healthy"]
    return package_alert(service,result)

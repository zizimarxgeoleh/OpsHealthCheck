def aggregate(reports):
    states = {}
    order = []
    for round_index, report in enumerate(reports, 1):
        for result in report["results"]:
            name = result["name"]
            if name not in states:
                order.append(name)
                states[name] = {"name":name,"observations":0,"healthy_observations":0,
                                "incidents":0,"recoveries":0,"last_healthy":None,"transitions":[]}
            state = states[name]
            healthy = result["healthy"]
            previous = state["last_healthy"]
            state["observations"] += 1
            state["healthy_observations"] += int(healthy)
            if not healthy:
                state["incidents"] += 1
                state["transitions"].append({"round":round_index,"event":"incident"})
            elif healthy and previous is False:
                state["recoveries"] += 1
                state["transitions"].append({"round":round_index,"event":"recovery"})
            state["last_healthy"] = healthy
    return [dict(states[name], availability_percent=round(100*states[name]["healthy_observations"]/len(reports),2)) for name in order]

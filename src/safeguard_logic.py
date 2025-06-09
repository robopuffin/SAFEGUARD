def evaluate_risk(agent, perceived):
    if perceived:
        agent.missed_detections = 0
        return "CLEAR"
    else:
        agent.missed_detections += 1
        if agent.missed_detections >= 3:
            agent.velocity = max(0.5, agent.velocity * 0.8)
            return "SAFEGUARD: CAUTION"
        else:
            return "MISS"

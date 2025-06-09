def evaluate_perception(perceived, agent):
    """
    Core SAFEGUARD logic:
    - Tracks perception failures
    - Triggers slowdown after 3 misses
    - Returns a string describing decision
    """
    if perceived:
        agent.missed_detections = 0
        return "CLEAR"
    else:
        agent.missed_detections += 1
        if agent.missed_detections >= 3:
            agent.velocity = max(0.5, agent.velocity * 0.8)
            return f"SAFEGUARD TRIGGERED: Velocity reduced to {agent.velocity:.2f}"
        else:
            return f"MISS #{agent.missed_detections}"

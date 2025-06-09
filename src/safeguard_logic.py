def decide_action(confidence, stopping_distance, distance_to_object):
    if confidence < 0.4 and stopping_distance >= distance_to_object:
        return 'ABORT'
    elif confidence < 0.6:
        return 'SLOW'
    else:
        return 'GO'

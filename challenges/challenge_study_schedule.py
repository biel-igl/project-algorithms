def study_schedule(permanence_period, target_time):
    counter = 0
    for this_tuple in permanence_period:
        if not (
            isinstance(this_tuple[0], int)
            and isinstance(this_tuple[1], int)
            and isinstance(target_time, int)
        ):
            return None
        if this_tuple[0] <= target_time <= this_tuple[1]:
            counter += 1
    return counter

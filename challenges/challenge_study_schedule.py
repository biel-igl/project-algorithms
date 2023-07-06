def study_schedule(permanence_period, target_time):
    period_dict = {}
    for this_tuple in permanence_period:
        if not (
            isinstance(this_tuple[0], int)
            and isinstance(this_tuple[1], int)
            and isinstance(target_time, int)
        ):
            return None
        else:
            lista = list(range(this_tuple[0], this_tuple[1] + 1))
            for number in lista:
                if number in period_dict:
                    period_dict[number] += 1
                else:
                    period_dict[number] = 1
    return period_dict[target_time]

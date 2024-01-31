def study_schedule(permanence_period, target_time):
    try:
        counter = 0
        for period_in, period_out in permanence_period:
            if period_in <= target_time <= period_out:
                counter += 1

        return counter
    except TypeError:
        return None

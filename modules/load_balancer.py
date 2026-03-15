def select_hospital(hospitals):

    # choose hospital with lowest load

    best = min(hospitals, key=lambda x: x["load"])

    return best
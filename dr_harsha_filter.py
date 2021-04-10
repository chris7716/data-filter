def filter_by_dr_harsha_filter(y, g):
    current_index = 1
    req_y = y.copy().tolist()
    while current_index < len(req_y):
        req_y[current_index] = g*(sum(y[0:current_index]) - sum(req_y[0:current_index-1]))
        current_index += 1
    return req_y
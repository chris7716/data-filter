def filter_by_moving_average_filter(y, window_size):
    current_index = window_size
    req_y = []
    while current_index < len(y) + 1:
        req_y.append((sum(y[(current_index - window_size): current_index - 1]))/window_size)
        current_index += 1
    return req_y
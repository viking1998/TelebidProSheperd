def check_capacity(capacity, weights, weights_used, trips_left, trips):
    if trips_left >= 0 and len(weights) == len(weights_used):
        print(capacity)
        return capacity
    if trips_left == 0 and len(weights) > len(weights_used):
        return 0
    current_weight_index = 0
    trip_capacity = capacity

    while current_weight_index < len(weights) and trip_capacity > 0:
        if current_weight_index not in weights_used and trip_capacity - weights[current_weight_index] >= 0:
            trip_capacity -= weights[current_weight_index]
            weights_used.append(current_weight_index)
        current_weight_index += 1

    if check_capacity(capacity, weights, weights_used, trips_left - 1, trips) == 0:
        if trips_left == trips:
            return check_capacity(capacity + 1, weights, [], trips, trips)
        else:
            return 0
    else:
        return capacity


first_input_line_split = input().split(" ")
num_goats = int(first_input_line_split[0])
max_trips = int(first_input_line_split[1])

goat_weights = list(map(int, input().split(" ")))
goat_weights.sort(reverse=True)
min_capacity = goat_weights[0]

check_capacity(min_capacity, goat_weights, [], max_trips, max_trips)

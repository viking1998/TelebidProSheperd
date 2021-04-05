def check_capacity(capacity, weights, weights_used, trips):
    for i in range(trips):
        temp_capacity = capacity
        current_weight_index = 0
        while current_weight_index < len(weights) and temp_capacity > 0:
            if current_weight_index not in weights_used and temp_capacity - weights[current_weight_index] >= 0:
                temp_capacity -= weights[current_weight_index]
                weights_used.append(current_weight_index)
            current_weight_index += 1
        if len(weights) == len(weights_used):
            return True
    return False


first_input_line_split = input().split(" ")
num_goats = int(first_input_line_split[0])
max_trips = int(first_input_line_split[1])

goat_weights = list(map(int, input().split(" ")))
goat_weights.sort(reverse=True)
min_capacity = goat_weights[0]

while True:
    if check_capacity(min_capacity, goat_weights, [], max_trips):
        print(min_capacity)
        break
    min_capacity += 1

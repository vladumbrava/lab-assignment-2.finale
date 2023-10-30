def add(score_list, value):
    if 10 <= value <= 100:
        score_list.append(value)
    return score_list

def insert_in_score_list(score_list, index, value):
    if 10 <= value <= 100:
        score_list.insert(index, value)
    return score_list

def remove(score_list, index):
    if 0 < index <= len(score_list):
        score_list.pop(index)
    return score_list

def remove_fromindex_toindex(score_list, from_index, to_index):
    if 0 < from_index < to_index <= len(score_list):
        score_list[from_index:to_index + 1] = []
    return score_list

def replace(score_list, index, new_value):
    score_list.pop(index)
    score_list.insert(index, new_value)
    return score_list

def less(score_list, value):
    new_list = []
    output_list = []
    for i in range(len(score_list)):
        if score_list[i] < value:
            new_list.append(i + 1)
    for i in range(len(new_list)):
        sufix = f"st participant" if new_list[i] == 1 else f"nd participant" if new_list[i] == 2 else f"rd participant" if new_list[i] == 3 else f"th participant"
        output_list.append(f"{new_list[i]}{sufix}")
    return output_list

def sorted_standings(score_list):
    participant_indices = list(range(len(score_list)))
    participant_indices.sort(key=lambda i: score_list[i], reverse=True)
    participant_place = []
    for i in range(len(participant_indices)):
        place = i + 1
        place_str = f"{place}st place: " if place == 1 else f"{place}nd place: " if place == 2 else f"{place}rd place: " if place == 3 else f"{place}th place: "
        participant_place.append(f"{place_str}{participant_indices[i] + 1}th participant")
    return participant_place

def sorted_higher(score_list, value):
    new_list = []
    for i,score in enumerate(score_list):
        if score > value:
            new_list.append((i, score))
    sorted_list = sorted(new_list, key=lambda x: x[1])
    output = [i for i, _ in sorted_list]
    return output

def avg(score_list, from_index, to_index):
    sum_of_scores = 0
    for i in range(from_index, to_index + 1):
        sum_of_scores += score_list[i]
    average = sum_of_scores / (to_index - from_index + 1)
    return average

def min(score_list, from_index, to_index):
    my_list = []
    for i in range(from_index, to_index + 1):
        my_list.append(score_list[i])
    my_list.sort()
    return my_list[0]

def mul(score_list, value, from_index, to_index):
    mul_list = []
    for i in range(from_index, to_index + 1):
        if score_list[i] % value == 0:
            mul_list.append(score_list[i])
    return mul_list

def filter_mul(score_list, value):
    new_list = []
    for score in score_list:
        if score % value == 0:
            new_list.append(score)
    return new_list

def filter_greater(score_list, value):
    filtered_list = []
    for score in score_list:
        if score > value:
            filtered_list.append(score)
    return filtered_list


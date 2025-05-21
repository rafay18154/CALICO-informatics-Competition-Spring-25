user_cases = int(input())

for _ in range(user_cases):
    val_str = input().strip()
    length = len(val_str)

    start_with_w = [0] * (length + 1)
    for index in range(length):
        start_with_w[index + 1] = start_with_w[index] + (1 if val_str[index] == 'w' else 0)

    how_many_u = []
    for index in range(length):
        if val_str[index] == 'u':
            how_many_u.append(index)

    valid_pairs = 0
    total_u = len(how_many_u)

    for i in range(total_u):
        for j in range(i + 1, total_u):
            left_hand = how_many_u[i] + 1
            right_hand = how_many_u[j] - 1
            if left_hand <= right_hand and start_with_w[right_hand + 1] - start_with_w[left_hand] > 0:
                valid_pairs += 1

    print(valid_pairs)
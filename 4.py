def best_path_to_buttons(T, test_cases):
    Outcomes = []
    for case in test_cases:
        N, M, grid = case
        position = {}
        for row in range(N):
            for col in range(M):
                position[grid[row][col]] = (row, col)
        
        where_to_go = 0
        c_row, c_col = 0, 0
        
        for num in range(1, N*M + 1):
            target_row, target_col = position[num]
            vertical = min(abs(c_row - target_row), N - abs(c_row - target_row))
            horizontal = min(abs(c_col - target_col), M - abs(c_col - target_col))
            where_to_go += vertical + horizontal
            c_row, c_col = target_row, target_col
        
        Outcomes.append(where_to_go)
    return Outcomes

T = int(input())
test_cases = []
for _ in range(T):
    N, M = map(int, input().split())
    grid = []
    for _ in range(N):
        row = list(map(int, input().split()))
        grid.append(row)
    test_cases.append((N, M, grid))


final_answers = best_path_to_buttons(T, test_cases)

for out_come in final_answers:
    print(out_come)
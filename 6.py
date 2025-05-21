def solve(N: int, M: int, S: str, G: list) -> int:

    # 1) Map each label to its (row, col) for O(1) lookups
    best_possible_label = {}
    for row in range(N):
        for col in range(M):
            best_possible_label[G[row][col]] = (row, col)
    
    # 2) Pre‐set your drift deltas
    drift_moves = {
        'U': (-1,  0),
        'D': ( 1,  0),
        'L': ( 0, -1),
        'R': ( 0,  1),
    }
    drift_length = len(S)
    
    check_total_number_of_moves = 0
    total_number_of_presnet_row, total_number_of_presnet_col = 0, 0  # start at G[0][0]
    present_working_phase = 0  # which drift-index we are on
    
    # 3) For each label in ascending order, find min k so that
    #    after k combined (action+drift) moves you can supply
    #    up to k steps of “action” to land exactly on the target.
    for label in range(1, N * M + 1):
        target_row, target_col = best_possible_label[label]
        
        # accumulate drift over k steps and check reachability
        check_possible_drift_in_row = 0
        check_possible_drift_in_col = 0
        k = 0
        while True:
            # “no‐action” position after k drifts
            check_verify_action_in_row = (total_number_of_presnet_row + check_possible_drift_in_row) % N
            check_verify_action_in_col = (total_number_of_presnet_col + check_possible_drift_in_col) % M
            
            # toroidal Manhattan distance to target
            dr = abs(check_verify_action_in_row - target_row)
            dr = min(dr, N - dr)
            dc = abs(check_verify_action_in_col - target_col)
            dc = min(dc, M - dc)
            required_actions = dr + dc
            
            # if we can supply that many action‐moves in k steps, we're done
            if required_actions <= k:
                break
            
            # otherwise, take one more drift step
            drift_index = (present_working_phase + k) % drift_length
            delta_row, delta_col = drift_moves[S[drift_index]]
            check_possible_drift_in_row += delta_row
            check_possible_drift_in_col += delta_col
            k += 1
        
        # commit those k actions
        check_total_number_of_moves += k
        # now we “teleport” exactly onto the target
        total_number_of_presnet_row, total_number_of_presnet_col = target_row, target_col
        present_working_phase = (present_working_phase + k) % drift_length
    
    return check_total_number_of_moves


def main():
    T = int(input())
    for _ in range(T):
        n, m = map(int, input().split())
        drift_sequence = input().strip()
        grid = [list(map(int, input().split())) for __ in range(n)]
        print(solve(n, m, drift_sequence, grid))


if __name__ == '__main__':
    main()
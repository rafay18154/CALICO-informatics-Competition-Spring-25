import sys
import threading
def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        large_number_of_blocks = []
        for _ in range(N):
            x0, y0, x1, y1 = map(int, sys.stdin.readline().split())
            mass = (x1 - x0) * (y1 - y0)
            cx = (x0 + x1) / 2
            cy = (y0 + y1) / 2
            large_number_of_blocks.append({'x0': x0, 'y0': y0, 'x1': x1, 'y1': y1, 'mass': mass, 'cx': cx, 'cy': cy})
        parent_avaliable = [-1] * N
        if_parent_children_yes = [[] for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                if large_number_of_blocks[i]['y0'] == large_number_of_blocks[j]['y1']:  # i sits on top of j
                    # Check x-overlap
                    if not (large_number_of_blocks[i]['x1'] <= large_number_of_blocks[j]['x0'] or large_number_of_blocks[i]['x0'] >= large_number_of_blocks[j]['x1']):
                        parent_avaliable[i] = j
                        if_parent_children_yes[j].append(i)
                        break
        stable = True
        def dfs(u):
            nonlocal stable
            total_mass = large_number_of_blocks[u]['mass']
            total_cx = large_number_of_blocks[u]['mass'] * large_number_of_blocks[u]['cx']
            total_cy = large_number_of_blocks[u]['mass'] * large_number_of_blocks[u]['cy']
            for v in if_parent_children_yes[u]:
                m, cx, cy = dfs(v)
                total_mass += m
                total_cx += m * cx
                total_cy += m * cy
            if parent_avaliable[u] != -1:
                check_status = parent_avaliable[u]
                center_x = total_cx / total_mass
                if not (large_number_of_blocks[check_status]['x0'] <= center_x <= large_number_of_blocks[check_status]['x1']):
                    stable = False
            return total_mass, total_cx / total_mass, total_cy / total_mass
        for i in range(N):
            if parent_avaliable[i] == -1 and large_number_of_blocks[i]['y0'] == 0:
                dfs(i)
        print("Stable" if stable else "Unstable")
threading.Thread(target=main).start()
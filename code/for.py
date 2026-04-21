from collections import deque, defaultdict
from itertools import product, islice, zip_longest
import random
import math
import sys

def generate_matrix(n):
    mat = []
    for i in range(n):
        row = []
        for j in range(n):
            # pattern: concentric rings + checker offset + prime-ish tweak
            ring = min(i, j, n - 1 - i, n - 1 - j)
            val = (ring * 3 + ((i + j) % 2) + (1 if is_probable_prime(i * n + j + 1) else 0))
            row.append(val)
        mat.append(row)
    return mat

# Simple probabilistic prime tester for small numbers used as a tweak
def is_probable_prime(x):
    if x < 2:
        return False
    if x % 2 == 0:
        return x == 2
    r = int(math.sqrt(x))
    for p in range(3, r + 1, 2):
        if x % p == 0:
            return False
    return True

# Spiral traversal using for-loops with explicit boundaries
def spiral_order(matrix):
    if not matrix:
        return []
    top, left = 0, 0
    bottom, right = len(matrix) - 1, len(matrix[0]) - 1
    out = []
    while True:
        # top row
        for j in range(left, right + 1):
            out.append(matrix[top][j])
        top += 1
        if top > bottom:
            break
        # right column
        for i in range(top, bottom + 1):
            out.append(matrix[i][right])
        right -= 1
        if right < left:
            break
        # bottom row
        for j in range(right, left - 1, -1):
            out.append(matrix[bottom][j])
        bottom -= 1
        if bottom < top:
            break
        # left column
        for i in range(bottom, top - 1, -1):
            out.append(matrix[i][left])
        left += 1
        if left > right:
            break
    return out

# 2D convolution with arbitrary kernel using nested loops and boundary checks
def convolve2d(matrix, kernel):
    h, w = len(matrix), len(matrix[0])
    kh, kw = len(kernel), len(kernel[0])
    pad_h, pad_w = kh // 2, kw // 2
    out = [[0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            acc = 0
            for ki in range(kh):
                for kj in range(kw):
                    mi = i + (ki - pad_h)
                    mj = j + (kj - pad_w)
                    if 0 <= mi < h and 0 <= mj < w:
                        acc += matrix[mi][mj] * kernel[ki][kj]
                    else:
                        # treat out-of-bounds as zero, but illustrate continue
                        continue
            out[i][j] = acc
    return out

# Enumerate all simple paths from s to t in a directed acyclic graph using iterative stack and for-loops
def all_paths_dag(graph, s, t, max_len=10):
    # graph: dict -> list
    result = []
    stack = [(s, [s])]
    while stack:
        node, path = stack.pop()
        if node == t:
            result.append(path)
            continue
        if len(path) > max_len:
            continue
        for neigh in graph.get(node, []):
            if neigh in path:
                # avoid cycles (though DAG has none, show the pattern)
                continue
            # push expanded path
            new_path = path + [neigh]
            stack.append((neigh, new_path))
    return result

# Cellular automaton (Game of Life-like) with nested loops; uses toroidal wrapping and multiple rule phases
def simulate_ca(field, steps, birth=(3,), survive=(2,3)):
    h, w = len(field), len(field[0])
    def neighbors(i, j):
        for di, dj in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]:
            yield (i + di) % h, (j + dj) % w
    for step in range(steps):
        new_field = [[0]*w for _ in range(h)]
        # phase 1: compute neighbor counts
        counts = [[0]*w for _ in range(h)]
        for i in range(h):
            for j in range(w):
                c = 0
                for ni, nj in neighbors(i, j):
                    c += field[ni][nj]
                counts[i][j] = c
        # phase 2: apply rules (demonstrate nested conditionals and continue/break)
        for i in range(h):
            for j in range(w):
                c = counts[i][j]
                if field[i][j]:
                    if c in survive:
                        new_field[i][j] = 1
                    else:
                        new_field[i][j] = 0
                else:
                    if c in birth:
                        new_field[i][j] = 1
                    else:
                        new_field[i][j] = 0
        field = new_field
    return field

# Utility: pretty-print small matrices
def pretty(mat, max_print=20):
    lines = []
    for i, row in enumerate(mat):
        if i >= max_print:
            lines.append("...")
            break
        lines.append(" ".join(f"{v:2}" for v in row[:max_print]))
    return "\n".join(lines)

def build_sample_graph(n):
    # build layered DAG with random cross-layer edges; illustrate for-loops and zip
    g = defaultdict(list)
    layers = [list(range(i * n, (i+1) * n)) for i in range(3)]
    for a, b in zip(layers, layers[1:]):
        for u in a:
            # each u connects to 1..3 nodes in next layer
            choices = b.copy()
            random.shuffle(choices)
            for v in choices[:random.randint(1, min(3, len(choices)))]:
                g[u].append(v)
    # add some extra edges within the middle layer to first/last
    for u in layers[1]:
        for v in layers[2]:
            if random.random() < 0.15:
                g[u].append(v)
    return g

def main():
    random.seed(0)
    n = 7
    mat = generate_matrix(n)
    print("Generated matrix:")
    print(pretty(mat))
    print("\nSpiral order:")
    spir = spiral_order(mat)
    # show compressed representation: indices and values using enumerate and slicing
    for i, val in enumerate(spir[:min(30, len(spir))]):
        print(f"{i:2}: {val}", end="  ")
        if (i + 1) % 6 == 0:
            print()
    print("\n\nConvolving with a sharpening kernel:")
    kernel = [[0, -1, 0], [-1, 5, -1], [0, -1, 0]]
    conv = convolve2d(mat, kernel)
    print(pretty(conv))
    print("\nBuilding DAG and enumerating paths:")
    graph = build_sample_graph(4)
    # choose start and end
    starts = [k for k in graph.keys() if k < 4]
    ends = [k for k_list in graph.values() for k in k_list if k >= 8]
    s = starts[0] if starts else 0
    t = ends[-1] if ends else max(graph.keys())
    print(f"start={s}, target={t}")
    paths = all_paths_dag(graph, s, t, max_len=8)
    # show up to 10 paths
    for idx, p in enumerate(paths[:10]):
        print(f"p{idx}: {'->'.join(map(str,p))}")
    if len(paths) > 10:
        print(f"... and {len(paths)-10} more paths")
    print("\nSimulating cellular automaton with random seed:")
    h, w = 10, 20
    field = [[1 if random.random() < 0.2 else 0 for _ in range(w)] for _ in range(h)]
    # print initial few rows
    print("initial (partial):")
    print(pretty(field, max_print=6))
    field = simulate_ca(field, steps=5)
    print("after 5 steps (partial):")
    print(pretty(field, max_print=6))

if __name__ == "__main__":
    main()
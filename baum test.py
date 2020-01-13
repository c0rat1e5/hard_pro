def dfs(start: int) -> int:
    stack = [(start, -1)]
    seen[start] = 1
    while stack:
        v, p = stack.pop()
        for u in T[v]:
            if u == p:
                continue
            if not seen[u]:
                stack.append((u, v))
                seen[u] = 1
            else:  # have a cycle
                return 0
    return 1  # subgraph is tree


def main():
    global T, seen
    N, M, *E = map(int, open(0).read().split())
    T = [[] for _ in range(N + 1)]
    for v, u in zip(*[iter(E)] * 2):
        T[v].append(u), T[u].append(v)
    ans, seen = 0, [0] * (N + 1)
    for v in range(1, N + 1):
        if not seen[v]:
            ans += dfs(v)
    print(ans)


if __name__ == "__main__":
    main()

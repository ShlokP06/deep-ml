def transpose_matrix(a: list[list[int | float]]) -> list[list[int | float]]:
    if not a:
        return []

    m, n = len(a), len(a[0])
    res = [[0] * m for _ in range(n)]

    for i in range(m):
        for j in range(n):
            res[j][i] = a[i][j]

    return res
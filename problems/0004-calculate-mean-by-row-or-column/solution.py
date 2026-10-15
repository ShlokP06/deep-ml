def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    m, n = len(matrix), len(matrix[0])
    a = []
    if mode.lower() == "column":
        for j in range(n):
            sm = 0
            for i in range(m):
                sm += matrix[i][j]
            a.append(sm / m)
    elif mode.lower() == "row":
        for i in range(m):
            sm = 0
            for j in range(n):
                sm += matrix[i][j]
            a.append(sm / n)
    return a
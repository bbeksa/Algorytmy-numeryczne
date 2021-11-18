def gauss_elimination(a, n):
    x = [0.0] * n
    for i in range(n):
        if a[i][i] == 0.0:
            raise ZeroDivisionError

        for j in range(i + 1, n):
            ratio = a[j][i] / a[i][i]

            for k in range(n + 1):
                a[j][k] = a[j][k] - ratio * a[i][k]

    for i in range(n - 2, -1, -1):
        x[n - 1] = a[n - 1][n] / a[n - 1][n - 1]
        x[i] = a[i][n]

        for j in range(i + 1, n):
            x[i] = x[i] - a[i][j] * x[j]

        x[i] = x[i] / a[i][i]

    return x
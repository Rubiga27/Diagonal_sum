def sum_main_diagonal(matrix):
    n = len(matrix)
    diagonal_sum = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                diagonal_sum += matrix[i][j]
    return diagonal_sum
rows, columns = map(int, input().split())
matrix = []
for _ in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)
diagonal_sum = sum_main_diagonal(matrix)
print(diagonal_sum)



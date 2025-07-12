def generate_magic_square(n):
    magic = [[0]*n for _ in range(n)]
    i, j = 0, n//2

    for num in range(1, n*n+1):
        magic[i][j] = num
        i2, j2 = (i-1) % n, (j+1) % n
        if magic[i2][j2]:
            i += 1
        else:
            i, j = i2, j2

    for row in magic:
        print(row)

generate_magic_square(3)

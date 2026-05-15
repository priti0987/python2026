# Magic Square Program (Odd Size)

n = int(input("Enter odd number size: "))

magic_square = [[0] * n for _ in range(n)]

num = 1
i = 0
j = n // 2

while num <= n * n:
    magic_square[i][j] = num
    num += 1

    new_i = (i - 1) % n
    new_j = (j + 1) % n

    if magic_square[new_i][new_j]:
        i = (i + 1) % n
    else:
        i = new_i
        j = new_j

print("\nMagic Square:\n")

for row in magic_square:
    for val in row:
        print(val, end="\t")
    print()

print("\nMagic Sum =", n * (n * n + 1) // 2)
# Python program to add two matrices using nested loop
x = [[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]
y = [[5, 8, 1],
    [6, 7, 3],
    [4, 5, 9]]

result = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

print("Using nested loop")

# Iterate through rows
for i in range(len(x)):
    # Iterate through columns
    for j in range(len(x[0])):
        result[i][j] = x[i][j] + y[i][j]

for r in result:
    print(r)

print("\n\nUsing list comprehension")
xl = [[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]
yl = [[5, 8, 1],
    [6, 7, 3],
    [4, 5, 9]]

res = [[xl[i][j] + yl[i][j] for j in range(len(xl[0]))] for i in range(len(xl))]
for r in res:
    print(r)

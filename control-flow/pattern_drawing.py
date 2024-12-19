user = int(input("Enter the size fo the pattern: "))
row = 0

while row < user:
    for _ in range(user):
        print("*", end="")
    print()
    row += 1

# nahom = 10

# while nahom >= 0:
#     elsa = 14
#     while elsa < nahom:
#         print("*", end="")
#         elsa += 1
#     print()
#     nahom -= 1


# name = 10
# row = 1
# while name >= row:
#     space = name - row
#     j = 1
#     while j <= space:
#         print(" ", end="")
#         j += 1
#     k = 1
#     while k <= (2 * row - 1):
#         print("*", end="")
#         k += 1
#     print()
#     row += 1
    
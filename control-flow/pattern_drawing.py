size = int(input("Enter the size of the pattern: "))

if size <= 0:
    print("Please enter a positive integer.")
    

    # Step 2: Draw the pattern using while and nested for loops
row = 0
while row < size:
    for _ in range(size):
        print("*", end="")
    print()  # Move to the next line after completing a row
    row += 1











# Size = int(input("Enter the size fo the pattern: "))
# Row = 0

# while Row < Size:
#     for _ in range(Size):
#         print("*", end="")
#     print()
#     Row += 1

# # nahom = 10

# # while nahom >= 0:
# #     elsa = 14
# #     while elsa < nahom:
# #         print("*", end="")
# #         elsa += 1
# #     print()
# #     nahom -= 1


# # name = 10
# # row = 1
# # while name >= row:
# #     space = name - row
# #     j = 1
# #     while j <= space:
# #         print(" ", end="")
# #         j += 1
# #     k = 1
# #     while k <= (2 * row - 1):
# #         print("*", end="")
# #         k += 1
# #     print()
# #     row += 1
    
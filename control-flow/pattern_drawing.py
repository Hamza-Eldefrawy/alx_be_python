size = int(input("Enter the size of the pattern: "))
i = size
while i:
    for j in range(size):
        print("*", end="")
    print()
    i -= 1


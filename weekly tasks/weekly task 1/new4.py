

# Step 1: Take inputs
n = int(input("Enter the length of the identifiers: "))
chars = []
print(f"Enter {n} characters one by one:")
for i in range(n):
    chars.append(input(f"Character {i+1}: "))

# Step 2: Initialize
indexes = [0] * n
total = len(chars) ** n

# Step 3: Generate all combinations
for _ in range(total):
    word = ""
    for i in indexes:
        word += chars[i]

    # Step 5: Increment indexes (simulate counting)
    pos = n - 1
    while pos >= 0:
        indexes[pos] += 1
        if indexes[pos] < len(chars):
            break
        indexes[pos] = 0
        pos -= 1



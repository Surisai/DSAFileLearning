# --- For Loop with range ---
print("=== For Loop with range ===")
for i in range(1, 6):
    print("Number:", i)

# --- For Loop over a List ---
print("\n=== For Loop over a List ===")
colors = ["red", "green", "blue"]
for color in colors:
    print("Color:", color)

# --- For Loop with enumerate ---
#enumerate() is a built-in Python function that lets you loop over a list 
#and get both the index and the value at the same time.
print("\n=== For Loop with enumerate ===")
grades = [85, 90, 78]
for index, grade in enumerate(grades):
    print(f"Student {index + 1} got: {grade}")

# --- For Loop with continue (skip even numbers) ---
print("\n=== For Loop with continue ===")
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print("Odd:", i)

# --- While Loop (counting up) ---
print("\n=== While Loop ===")
count = 1
while count <= 5:
    print("Count:", count)
    count += 1

# --- While Loop with break (find first number divisible by 7) ---
print("\n=== While Loop with break ===")
num = 10
while True:
    if num % 7 == 0:
        print("First divisible by 7:", num)
        break
    num += 1

# --- Nested Loops (Multiplication Table) ---
print("\n=== Nested Loops (Multiplication Table 1-3) ===")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print("---")


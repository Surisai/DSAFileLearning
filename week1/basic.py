#Data Types, Lists, Strings, Loops, and Advanced Slicing
## --- Data Types ---
name = "Alice"       # string
age = 20             # int
height = 5.6         # float
is_enrolled = True   # bool

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Enrolled?", is_enrolled)

# --- List Declaration ---
marks = [75, 83, 91, 68, 89, 77, 94]

# --- List Access & Slicing ---
print("\n--- List Slicing ---")
print("Original list:", marks)
print("marks[:]:", marks[:])              # entire list
print("marks[::2]:", marks[::2])          # every 2nd element
print("marks[::-1]:", marks[::-1])        # reversed list
print("marks[2:]:", marks[2:])            # from index 2 to end
print("marks[:4]:", marks[:4])            # from start to index 3
print("marks[1:5]:", marks[1:5])          # index 1 to 4
print("marks[:-1]:", marks[:-1])          # all except last
print("marks[-3:]:", marks[-3:])          # last 3 elements

# --- List Comprehension ---
bonus_marks = [m + 5 for m in marks]
print("\nBonus Marks (list comprehension):", bonus_marks)

# --- Sorting ---
sorted_marks = sorted(marks)
print("Sorted marks (non-destructive):", sorted_marks)
marks.sort()
print("Sorted marks (in-place):", marks)

# --- Loops ---
print("\n--- For Loop ---")
print("All marks:")
for mark in marks:
    print(mark)

# Average using loop
total = 0
for m in marks:
    total += m
average = total / len(marks)
print("Average mark:", average)

print("\n--- While Loop ---")
print("Marks > 80:")
i = 0
while i < len(marks):
    if marks[i] > 80:
        print(marks[i])
    i += 1

# --- String Operations ---
print("\n--- String Operations ---")
message = "Welcome to Python"
print("Original:", message)
print("Lowercase:", message.lower())
print("Split words:", message.split())
print("Reversed string:", message[::-1])
print("First 7 characters:", message[:7])
print("Characters from index 3:", message[3:])
print("Every 2nd character:", message[::2])


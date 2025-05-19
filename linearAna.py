#linear Analysis with Boolean condition
# Online Python compiler (interpreter) to run Python online.



def linear_search(my_list, key):
    for i in range(0, len(my_list)):
        print(f"Comparing {my_list[i]} with {key}") # comaparing the list and the key
        if my_list[i] == key:
            print(f"Found at index {i}")
            return i
    print("Not found")
    return -1

# Test with n = 10
my_list = [5, 8, 2, 9, 0, 3, 1, 6, 7, 4]
linear_search(my_list, 3)   # Expected: index 5
linear_search(my_list, 99)  # Expected: not found (-1)


# def linear_search(my_list, key):
#     for item in my_list:
#         if item == key:
#             return 1  # found
#     return 0  # not found


# Testing with integers
numbers = [10, 20, 30, 40, 50]

print(linear_search(numbers, 30))   # Expected output: 2
print(linear_search(numbers, 100))  # Expected output: -1

# Testing with strings
fruits = ["apple", "banana", "cherry", "date"]

print(linear_search(fruits, "cherry"))  # Expected output: 2
print(linear_search(fruits, "kiwi"))    # Expected output: -1

def test_linear_search():
    assert linear_search([1, 2, 3, 4], 3) == 2
    assert linear_search([1, 2, 3, 4], 5) == -1
    assert linear_search(["a", "b", "c"], "c") == 2
    assert linear_search(["a", "b", "c"], "z") == -1
    assert linear_search([], 1) == -1  # Edge case: empty list

    print("All tests passed!")

test_linear_search()



class Item:
    def __init__(self, id):
        self.id = id

    def __eq__(self, other):
        return isinstance(other, Item) and self.id == other.id

items = [Item(1), Item(2), Item(3), Item(4),Item(5)]
print(linear_search(items, Item(2)))  # Expected output: 1
print(linear_search(items, Item(6)))  # Expected output: -1

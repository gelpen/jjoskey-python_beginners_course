numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

numbers.reverse()
print(numbers)  # Outputs: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

new_numbers = numbers[::-1]
print(new_numbers)  # Outputs: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(numbers)


numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new_numbers = reversed(numbers)
print(type(new_numbers))
print(new_numbers)
new_numbers = list(new_numbers)
print(type(new_numbers))
print(new_numbers)  # Outputs: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

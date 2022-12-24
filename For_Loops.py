for items in ['Madan', 'Ram', 'Mosh']:
    print(items)
for numbers in range(10,100):
    print(numbers)
for numbers in range(10, 100, 10):
        print(numbers)
# Write a program to print the items in the shopping cart and calculate the total cost of all the elents in imaginary shopping cart
items = [250, 300, 400, 200, 1000, 500]
sum = 0
for price in items:
    sum += price
print(f"The Total price is:{sum}")
# Nested_Loops_________________________________________________
for x in range(4):
    for y in range(3):
        print(f'({x},{y})')
# Draw a F figure like shape using 'x' al-phabet character.
numbers = [5, 2, 5, 2, 2]
for iterate in numbers:
    output = ''
    for count in range(iterate):
        output += 'x'
    print(output)
# 2D Lists'
# Remove duplicates:
numbers = [5, 5, 2, 1, 7, 4, 4]
uniques= []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

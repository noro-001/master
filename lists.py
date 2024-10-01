####EmptyLists####
# empty = []

# empty.append(int(input("Enter first digit: ")))
# empty.append(int(input("Enter second digit: ")))
# empty.append(int(input("Enter third digit: ")))
# empty.append(int(input("Enter fourth digit: ")))
# empty.append(int(input("Enter fivth digit: ")))

# print(empty)

####sortAndDelete####
# fruits = ["banana", "apple", "cherry", "watermelon", "kiwi"]

# fruits.sort()

# del fruits[0]
# del fruits[3]

# print(fruits)

####integers####
numbers = [1, 23, 5, 4, 1, 5, 4, 20, 11, 14, 46]

numbers.sort()
numbers = list(dict.fromkeys(numbers))

print(numbers)

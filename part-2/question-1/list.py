list1 = [1,2,2,3,4,5,6,6,7,8,9,9,10]

unique_values = set(list1)
new_list = list(unique_values)
print("Original List : ", list1)
print("Unique values : ", unique_values)
print("New List : ", new_list)

reading_numbers = [x for x in range(1,11)]
print("Read values : ", reading_numbers)
even_numbers = [x for x in reading_numbers if x % 2 == 0]
print('Even numbers are as : ', even_numbers)

# reverse modify the original list
even_numbers.reverse()
print("Reversed numbers : ", even_numbers)
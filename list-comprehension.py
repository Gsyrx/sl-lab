list_data = [1, 2, 3, 4, 4, 5, 6, 7, 7, 8]
print("Original list = ", list_data)

new_list = [x for x in list_data if x % 2 == 0]

print("New List = ", new_list)

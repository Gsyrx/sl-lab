# creating list
list = []

size = int(input("Enter the size of list : "))

for i in range(size):
  data = int(input("Enter the data : "))
  list.append(data)

print("Data in the list = ", list)

# min and max
minimum = min(list)
maximum = max(list)
print("Minimum value = ", minimum)
print("Maximum value = ", maximum)

# inserting new elements
new_element = int(input("Enter new element = "))
position = int(input("Enter the position = "))

list.insert(position,new_element)
print("New list = ", list)


# delete element
deleted_element = int(input("Enter the number to be deleted = "))
list.remove(deleted_element)

print("New list = ", list)

# present or not
value = int(input("Enter the number to be checked = "))

if value in list:
  print("Number is found at index ", list.index(value))
else:
  print("Number not found")
list = [];

size = int(input("Enter the size of the list : "))

for i in range(0,size):
  data = int(input("Enter the data to be inserted : "))
  list.append(data)
print("Data in the list  : ", list);

minimum = min(list)
maximum = max(list)
print("The minimum value in the list : ",minimum)
print("The maximum value in the list : ",maximum)

new_element = int(input("Enter new element to br inserted : "))
position = int(input("Enter the position to be inserted : "))
list.insert(position,new_element)
print("New data in the list : ",list)

removed_element = int(input("Enter the element to be removed : "))
list.remove(removed_element)
print("New list after removing elements : ", list)

value = int(input("Enter the number to be determined : "))
if value in list:
  print("Element is found at index : ", list.index(value))
else:
  print("Element not found")
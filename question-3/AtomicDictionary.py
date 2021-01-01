def AtomicDictionary():
  print("Original elements : ")
  elements = {"C": "Carbon", "B": "Boron", "S":"Sulphur", "N": "Nitrogen"}
  print(elements)
  new_symbol = input("Enter new symbol to be added : ")
  new_element = input("Enter value for new symbol : ")

  if new_symbol in elements.keys():
    print("Key exist, new value is inserted !!")
  else:
    print("Key does not exist, and added to the dictionary")
  elements[new_symbol] = new_element
  print(elements)
  print("Length of dictionary : ", len(elements))

  search_key = input("Enter the key to be searched : ")
  if search_key in elements.keys():
    print("Key is present and its value is : ", elements[search_key])
  else:
    print("Key does not exist in the dictionary !!")
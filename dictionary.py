dictionary = {
    1:'Amazon',
    2:'Flipkart',
    3:'Snapdeal',
    4:'Myntra'
  }

print(dictionary)
print(dictionary[1])

del dictionary[4]
print(dictionary)

print("List of key value pairs",dictionary.items()) # array of key value pair

print("List of keys",dictionary.keys()) # array of keys

print("List of values",dictionary.values()) # array of values

copy = dictionary.copy()
print("Shallow copy of dictionary" , copy)

dictionary.clear()
print("Trying to print an empty dictionary" , dictionary)

# from collections import Counter
# def word_count(fname):
#   with open(fname) as f:
#     return Counter(f.read().split())
# print("Number of words in the file :",word_count("test.txt"))

fd = open("./test.txt")
file = fd.read()

dict = {}

for word in file.split():
  dict[word] = dict.get(word,0) + 1
print(dict)
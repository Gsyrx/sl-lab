from functools import reduce
fd=open("./text.txt")
file = fd.read()
print(file)



dict={}

for word in file.split():
    dict[word] = dict.get(word,0) + 1
print(dict)
print("<----->")


sortedDict = sorted(dict.items(), key=lambda dictItem: dictItem[1], reverse=True)
for i in range(10):
	print(sortedDict[i])

print(dict.items())

wordLen= []
for item in dict.items():
    wordLen.append(len(item[0]))

print(wordLen)


# Write a one-line reduce function to get the average length

sum = reduce(lambda x,y: x+y, wordLen)
print ("Average length of words: " , sum/len(wordLen))


# Write a one-line list comprehension to display squares of all odd numbers

squares = [x**2 for x in wordLen if x%2 != 0]
print ("Squres of odd word lengths: ")
print (squares)
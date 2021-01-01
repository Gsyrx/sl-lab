from functools import reduce

my_list = [1,2,3,4,5,6]
print("Original list : ", my_list)

new_list = [x*3 for x in my_list]
print("New List : ", new_list)

reduced_my_list = reduce(lambda x,y: x+y, my_list)
print("Reduced my_list : ",reduced_my_list)

reduced_new_list = reduce(lambda x,y: x+y, new_list)
print("Reduced new_list : ", reduced_new_list)



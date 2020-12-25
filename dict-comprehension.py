square_dict = {num: num*num for num in range(1, 11)}
print(square_dict)

# same output without using dict-comprehension
# square_dict = dict()
# for num in range(1, 11):
#     square_dict[num] = num*num
# print(square_dict)
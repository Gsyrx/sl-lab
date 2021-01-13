def Max(list):
  if len(list) == 1:
    return list[0]
  else:
    maximum = Max(list[1:])
    return maximum if maximum > list[0] else list[0]

def main():
  try:
    list = eval(input("Enter a list of numbers : "))
    print("The largest number in the list : ", Max(list))
  except SyntaxError:
    print("Please enter comma seperated numbers")
  except:
    print("Enter only numbers")

main()
def celcius_to_farenheit(c1):
  return (c1 * (9/5) + 32)

def farenheit_to_celcius(f1):
  return ((f1 - 32) * (5/9))

def celcius_to_kelvin(c2):
  return (c2 + 273.15)

def kelvin_to_celcius(k1):
  return (k1 - 273.15)

def farenheit_to_kelvin(f2):
  return celcius_to_kelvin(farenheit_to_celcius(f2))

def kelvin_to_farenheit(k2):
  return celcius_to_farenheit(kelvin_to_celcius(k2))


select = 'y'

op1 = []
op2 = []
op3 = []
op4 = []
op5 = []
op6 = []

while(select == 'y' or select == 'Y'):
  print("\nDifferent options are as : \n 1 C -> F \n 2 F -> C\n 3 C -> K\n 4 K -> C\n 5 F -> K\n 6 K -> F")

  choice = int(input("Enter your choice : "))

  if (choice == 1 or choice == 2 or choice == 3 or choice == 4 or choice == 5 or choice == 6):

    if (choice == 1):
      c1 = float(input("Enter the temperature in celcius : "))
      op1 = op1 + [(c1, celcius_to_farenheit(c1))]
      print("Celcius to farenheit ")
      print(sorted(op1))

    elif (choice == 2):
      f1 = float(input("Enter the temperature in farenheit : "))
      op2 = op2 + [(f1, farenheit_to_celcius(f1))]
      print("Farenheit to celcius")
      print(sorted(op2))

    elif (choice == 3):
      c2 = float(input("Enter the temperature in celcius : "))
      op3 = op3 + [(c2, celcius_to_kelvin(c2))]
      print("Celcius to kelvin")
      print(sorted(op3))

    elif (choice == 4):
      k1 = float(input("Enter the temperature in kelvin : "))
      op4 = op4 + [(k1, kelvin_to_celcius(k1))]
      print("Kelvin to celcius")
      print(sorted(op4))

    elif (choice == 5):
      f2 = float(input("Enter the temperature in farenheit : "))
      op5 = op5 + [(f2, farenheit_to_kelvin(f2))]
      print("Farenheit to kelvin")
      print(sorted(op5))

    elif (choice == 6):
      k2 = float(input("Enter the temperature in kelvin : "))
      op6 = op6 + [(k2, kelvin_to_farenheit(k2))]
      print("Kelvin to farenheit")
      print(sorted(op6))

  else:
    print("Enter valid number !")

  select = input("Select y to continue or any other key to exit : ")
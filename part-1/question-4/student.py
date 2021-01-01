class Student:
  name = ""
  age = 0
  subjects_marks = []
  def __init__(self, name, age, subjects_marks):
    self.name = name
    self.age = age
    self.subjects_marks = subjects_marks

  def accept(self):
    self.name = input("Enter name : ")
    self.age = int(input("Enter age : "))
    marks = []
    for i in range(0,3):
      mark = int(input(f"Enter marks in subject {i+1} : "))
      marks.append(mark)
    self.subjects_marks = marks

  def display(self):
    print("Name : ", self.name)
    print("Age : ", self.age)
    print("Subject marks : ", self.subjects_marks)


s1 = Student("Gaurav",20,[80,90,85])
s1.display()
s1.accept()
s1.display()

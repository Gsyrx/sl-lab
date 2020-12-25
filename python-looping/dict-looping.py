def students_marks_average(list_of_students):
  for x in list_of_students:
    x1 = x.pop('m1')
    x2 = x.pop('m2')
    x['average'] = (x1 + x2) / 2
  return list_of_students

students = [
  {'id': 1, 'name': "Gaurav", "m1": 80, 'm2': 90},
  {'id': 2, 'name': "Akshat", "m1": 85, 'm2': 88},
  {'id': 3, 'name': "Aaryan", "m1": 40, 'm2': 45},
  {'id': 4, 'name': "Aman", "m1": 60, 'm2': 75},
]

print(students_marks_average(students))

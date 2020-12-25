# def sum_math_v_vi_average(list_of_dicts):
#     for d in list_of_dicts: 
#         n1 = d.pop('V')
#         n2 = d.pop('VI')
#         d['V+VI'] = (n1 + n2)/2
#     return list_of_dicts 
# student_details= [
#   {'id' : 1, 'subject' : 'math', 'V' : 70, 'VI' : 82},
#   {'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74},
#   {'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86}
# ]
# print(sum_math_v_vi_average(student_details))


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

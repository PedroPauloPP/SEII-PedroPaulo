student = {'name': 'PedroPaulo', 'age': 28, 'courses': ['Math', 'CompSci']}

print(student['name'])
print(student.get('phone', 'Not found'))

student['phone']= '5555-555'
student.update({'name: 'Miranda', 'age': 28, phone:'8260'})

del studen['age']
age = student.pop('age')
 

for key, value in student.items():
    print(key, value)
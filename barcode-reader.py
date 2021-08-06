import qrcode

# you can use this QR code reader to read the QR code(https://online-barcode-reader.inliteresearch.com/)


instructor = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'gender': 'Male',
    'skills': ['HTML', 'CSS', 'JS', 'React', 'Python', 'MongoDB'],
    'is_married': True,
    'address': {
        'country': 'Finland',
        'city': 'Helsinki'
    }
}

# List of dictionaries
students = [
    {'name': 'Adugna', 'gender': 'Male', 'country': 'USA'},
    {'name': 'Antony', 'gender': 'Male', 'country': 'USA'},
    {'name': 'Dereje', 'gender': 'Male', 'country': 'USA'},
    {'name': 'Fassica', 'gender': 'Female', 'country': 'USA'},
    {'name': 'Genet', 'gender': 'Female', 'country': 'USA'},
    {'name': 'John', 'gender': 'Male', 'country': 'USA'},
    {'name': 'Michael', 'gender': 'Male', 'country': 'USA'},
    {'name': 'Momina', 'gender': 'Female', 'country': 'USA'},
    {'name': 'Nebeyu', 'gender': 'Male', 'country': 'Ethiopia'},
    {'name': 'Tehetina', 'gender': 'Female', 'country': 'USA'},
    {'name': 'Sandy', 'gender': 'Male', 'country': 'Finland'},
]

course_info = {
    'name': 'Python Bootcamp',
    'instructor': 'Asabeneh Shitahun Yetayeh',
    'year': 2021,
    'starts_at': '1 August 2021',
    'ends_at': '31 August 2021',
    'is_started': True,
    'is_ended': False,
    'activities':['Lesson', 'Self Reading',
                           'Exercises', 'Group Project', 'Individual Projects'],
    'students':['Adugna', 'Antony', 'Dereje', 'Fassica', 'Genet', 'John', 'Michael', 'Momina', 'Nebeyu', 'Tehetina', 'Sandy']
}

names = list(map(lambda student: student['name'], students))
most_students = ', '.join(names[0:-1])
last_student = names[-1]
instructor_full_name = instructor['first_name'] + ' '+  instructor['last_name']
address = instructor['address']['country']

statement = f'There ara {len(students)} students in the Python Bootcamp. The students are {most_students}, and {last_student}. The instructor is {instructor_full_name}. He lives in {address}. If you want to know more about the instructor check this link(https://testimonify.herokuapp.com/).'
print(statement)

img = qrcode.make(statement)
img.save("barcode.jpg")




students = []

def add_student(name):
    students.append(name)

def view_students():
    for s in students:
        print(s)

add_student("Rahul")
add_student("Priya")

view_students()

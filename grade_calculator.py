name = input("Enter student's name: ")

Math = float(input("Enter marks for subject Mathematics: "))
English = float(input("Enter marks for subject English: "))
Python = float(input("Enter marks for subject Python: "))

marks = [Math, English, Python]

if any(m < 0 or m > 100 for m in marks):
    print("Invalid marks!")
else:
    average = (Math + English + Python) / 3

    if average >= 80:
        grade = "A+"
    elif average >= 70:
        grade = "A"
    elif average >= 60:
        grade = "A-"
    elif average >= 50:
        grade = "B"
    elif average >= 40:
        grade = "C"
    else:
        grade = "F"

    print("Student Name:", name)
    print("Average Marks:", round(average, 2))
    print("Final Grade:", grade)
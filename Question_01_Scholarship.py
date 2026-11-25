name = input("Enter student name: ")

aggregate = float(input("Enter aggregate marks: "))

subject1 = float(input("Enter subject 1 marks: "))
subject2 = float(input("Enter subject 2 marks: "))
subject3 = float(input("Enter subject 3 marks: "))

attendance = float(input("Enter attendance percentage: "))

income = float(input("Enter annual family income: "))

if (aggregate >= 75 and
    subject1 >= 60 and
    subject2 >= 60 and
    subject3 >= 60 and
    attendance >= 75 and
    income <= 300000):

    print("Student Name:", name)
    print("Eligible for Scholarship")

else:
    print("Student Name:", name)
    print("Not Eligible for Scholarship")
    
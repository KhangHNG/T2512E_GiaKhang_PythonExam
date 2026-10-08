if __name__ == '__main__':
    n = int(input("Enter number of students: "))
    print("\n")
    list_students = []
    for i in range (0, n):
        studentID = input("Enter student ID: ")
        fullName = input("Enter full name: ")
        pythonScore = float(input("Enter python score: "))
        print("\n")
        student = {"ID": studentID, "Name": fullName, "Score": pythonScore}
        list_students.append(student)

    # Display all
    for i in list_students:
        print(f"Student ID: {i["ID"]} - Name: {i["Name"]} - Score: {i["Score"]}")
    print("\n")

    # Student with highest score
    list_students.sort(key= lambda x: x["Score"], reverse= True)
    print(f"The student with the highest score is: {list_students[0]["ID"]} - {list_students[0]["Name"]} - {list_students[0]["Score"]}")
    print("\n")

    # Students who passed (Score >= 5)
    passed_students = []
    for i in list_students:
        if i["Score"] >= 5:
            passed_students.append(i)
    print("List of passed students:")
    for k in passed_students:
        print(f"Student ID: {k["ID"]} - Name: {k["Name"]} - Score: {k["Score"]}")
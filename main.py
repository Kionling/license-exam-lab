def getStudentAnswers():
    studentAnswers = []
    for i in range(10):
        studentAnswers.append(input("Enter the student's answer for question " + str(i + 1) + ": "))
    return studentAnswers

def getCorrectAnswers():
    correctAnswers = ["B", "D", "A", "A", "C", "A", "B", "A", "C", "D"]
    for i in range(10):
        correctAnswers.append(input("Enter the correct answer for question " + str(i + 1) + ": "))
    return correctAnswers
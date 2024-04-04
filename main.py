def getStudentAnswers():
    student_answers = []
    for i in range(1, 21):
        answer = 'A'  
        while answer not in ('A', 'B', 'C', 'D'):
            print("Invalid answer. Please enter A, B, C, or D.")
            answer = 'A'  
        student_answers.append(answer)
    return student_answers



def check_passed(student_answers):
    correct_answers = ['B', 'D', 'A', 'A', 'C', 'A', 'B', 'A', 'C', 'D', 'B', 'C', 'D', 'A', 'D', 'C', 'C', 'B', 'D', 'A']
    count_correct = 0
    missed_questions = []
    for i in range(len(student_answers)):
        if student_answers[i] == correct_answers[i]:
            count_correct += 1
        else:
            missed_questions.append(i + 1)
    passed = count_correct >= 15
    return passed, count_correct, missed_questions

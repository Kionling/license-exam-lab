def get_student_answers():
    student_answers = []
    for i in range(1, 21):
        answer = 'A'  
        while answer not in ('A', 'B', 'C', 'D'):
            print("Invalid answer. Please enter A, B, C, or D.")
            answer = 'A'  
        student_answers.append(answer)
    return student_answers
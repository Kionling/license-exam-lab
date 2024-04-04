def get_student_answers():
    student_answers = []
    for i in range(1, 21):
        answer = input(f"Enter answer for question {i} (A/B/C/D): ").strip().upper()
        while answer not in ('A', 'B', 'C', 'D'):
            print("Invalid answer. Please enter A, B, C, or D.")
            answer = input(f"Enter answer for question {i} (A/B/C/D): ").strip().upper()
        student_answers.append(answer)
    return student_answers

def check_passed(student_answers):
    correct_answers = ['B', 'D', 'A', 'A', 'C', 'A', 'B', 'A', 'C', 'D', 'B', 'C', 'D', 'A', 'D', 'C', 'C', 'B', 'D', 'A']
    count_correct = 0
    missed_questions = []
    for i, student_answer in enumerate(student_answers):
        if student_answer == correct_answers[i]:
            count_correct += 1
        else:
            missed_questions.append(i + 1)
    return count_correct >= 15, count_correct, missed_questions

def main():
    student_answers = get_student_answers()
    passed, total_correct, questions_missed = check_passed(student_answers)
    if passed:
        print("The student passed the exam.")
    else:
        print("The student failed the exam.")
    print("Total correct answers:", total_correct)
    print("Questions missed:", questions_missed)

if __name__ == '__main__':
    main()

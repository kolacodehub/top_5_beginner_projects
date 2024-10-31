def main():
    while True:
        questions = [
            '''
 1- Who is the president of Nigeria: 
    A - Muhammadu Buhari
    B - Bola Ahmed Tinubu
    C - Tiamiyu Abdulsalam
    D - Goodlick Ebele
            ''',
            '''
 2- Who is the govenor of Lagos state: 
    A - Ambode
    B - Bola Ahmed 
    C - Tiamiyu Abdulsalam
    D - Sanwo-olu
            ''',
            '''
 3- Who is the president of Al-Itqaan: 
    A - Muhammadu Buhari
    B - Bola Ahmed Tinubu
    C - Ishaq Abdul-azeez
    D - Goodlick Ebele
            ''',
            '''
 4- What is the capital of Nigeria: 
    A - Lagos
    B - Abuja
    C - Isolo
    D - Ikeja
            ''',
            '''
 5- What is the capital of Lagos: 
    A - Lagos
    B - Abuja
    C - Isolo
    D - Ikeja
            '''
            ]
        default_correct_answers = [0, 'B', 'D', 'C', 'B', 'D']
        user_input_answers = [0]
        user_correct_answers = []
        user_wrong_answers = []
        for question in questions:
            print(question)
            user_input = input('Enter your answer (a/b/c/d): ').capitalize()
            user_input_answers.append(user_input)
        for i in range(1, len(default_correct_answers)):
            if user_input_answers[i] == default_correct_answers[i]:
                user_correct_answers.append(f'Question {i} is correct')
            else:
                user_wrong_answers.append(f'You missed question {i}')

        print('Quiz Complete!!')

        print(f'Your score is {float(len(user_correct_answers))} / {float(len(questions))}')
        if len(user_wrong_answers) != 0:
            for i in user_wrong_answers:
                print(i)
        if float(len(user_correct_answers)) == float(len(questions)):
            print('Excellent')
        else:
            print('Advice: Try again next time')
        try_again = input('Will you like to try again (y/n): ').lower()
        print(try_again)
        if try_again == 'y':
            continue
        elif try_again == 'n':
            break
        else:
            try_again = input('Will you like to try again: (y/n)').lower()
            print('Enter y or n')
            print(try_again)
        break



if __name__ == '__main__':
    main()
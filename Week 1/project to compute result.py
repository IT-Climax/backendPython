


students_results = {}

def result_computations():
    try:
        students = int(input("How many students are there in your class?    "))
        for names in range(students):
            student_name = input("Enter student's Name: ")
            maths = int(input(f'Enter Mathematics score: '))
            eng = int(input(f'Enter English score: '))
            comp = int(input(f'Enter Computer score: '))

            scores = students_results[student_name][maths, eng, comp]
            total_scores = sum(scores)
            average_scores = total_scores/ len(scores)
            students_results[student_name] = {
            "ave" : average_scores
            }

        print(students_results)

            # for x, y in students_results.items():
            #     print(f'{x}, {y}')

    except ValueError:
        print('Enter number only')


result_computations()




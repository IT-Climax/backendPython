
students_result = {}

def result_compilation():

    try:
        students = int(input("How many students are there in your class? "))
        for s in range(students):
            student_name = input("Enter Student Name: ").title()
            maths = int(input("Enter Student Mathematics score: "))
            eng = int(input("Enter Student English score: "))
            comp = int(input("Enter Computer Science Score: "))

            # Student average score calc
            scores = [maths, eng, comp]
            total_score = sum(scores)
            avg_score = float(total_score / len(scores))

            # Store result in students_result dict
            students_result[student_name] = {
                'Mathematics': maths,
                'English': eng,
                'Computer Studies': comp,
                'Total':total_score,
                'Average': avg_score,
            }

        # Print result
        for student, result in students_result.items():
            print("===================================="
                  "======================================"
                  "======================================")
            print(f"Results for {student}: {result}")

            avg = result['Average']
            if avg >= 70.0:
                   print(f' {student} Grade is: A')
            elif 60.0 <= avg < 70.0:
                print(f'{student} Grade is: B')
            elif 50.0 <= avg < 60.0:
                 print(f' {student} Grade is: C')
            elif 40.0 <= avg < 50.0:
                 print(f'{student} Grade is:D')
            else:
                 print(f'{student} Grade is: F')


        for k, position in (students_result.items()):
            print(f'{k}, {position}')
            positions = position['Average']
            print(positions)

            sorted_dict = students_result(sorted(students_result.items(), key=lambda item: item[1] ))
            print(sorted_dict)

    except ValueError:
        print("Please enter numbers only for number of students and scores.")
    print(students_result)

    print("===================================="
          "======================================"
          "======================================")

    repeat = input(f'Would you like to continue? Yes(y)/No(n): ')
    if repeat == "y":
        result_compilation()
    else: exit()

result_compilation()
#print(students_result)
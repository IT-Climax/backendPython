students_cgpa ={
    "musa": 3.3,
    "umar": 2.2,
    "ismail": 2.1,
    # "zz": 3.4
    }

# total_v = 0

def students_ave():
    global aver
    total_v = 0
    for names, values in students_cgpa.items():
        total_v += values
        aver = total_v / len(students_cgpa)
        print(f"{names} : {values}")
    print(f"Class Average is :{aver: .2f}")
    # for value in students_cgpa.values():
    #     total = sum(students_cgpa.values())
    #     ave = total / len(students_cgpa)
    # print(f"{ave: .2f}")

    # total = sum(students_cgpa.values())
    # ave = total / len(students_cgpa)
    # print(f"{ave: .2f}")

students_ave()

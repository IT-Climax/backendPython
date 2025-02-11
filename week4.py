
        # PRESENTATION
        # NOTHING FROM CLASS
names = ['joe', 'jim', 'john']
scores = ['78', '86', '54']
with open('../texts.txt', 'w') as op:
    for i in range(0, 3):
        details = names[i] + '-' + scores[i]+'\n'
        op.write(details)


"""
student_record = {}
names = input("enter student name: ")
subjects = input("enter student subject: ")
grades = int(input("enter student grade: "))

student_record[names] = {}
student_record[names][subjects] = grades

with open('text.txt', 'a') as open_text:
    for i, j in student_record.items():
        open_text.write(f'{i}: {j}\n')


with open('text.txt', 'r') as open_text:
    for line in open_text:
        print(line.strip())
"""
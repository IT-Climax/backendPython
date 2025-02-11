def grade_range():
    global jamb
    try:
        if a=="a"and b=="a"and c=="a"and d=="a"and e=="a":
            jamb=int(input("enter your jamb score:"))
        elif a=="a"and b=="b"and c=="a"and d=="a"and e=="a":
            jamb=int(input("enter your jamb score:"))
        elif a=="a"and b=="a"and c=="b"and d=="a"and e=="a":
            jamb=int(input("enter your jamb score:"))
        elif a=="a"and b=="a"and c=="a"and d=="b"and e=="a":
            jamb=int(input("enter your jamb score:"))
        elif a=="a"and b=="a"and c=="a"and d=="a"and e=="b":
            jamb=int(input("enter your jamb score:"))
 
        else: print("sorry due to your grades you arent considered eligible for this scholarship you must have at least 4 A's")
    except ValueError: print("please enter your grades correctly")
def jamb_scores():
    if 260<=jamb<=400:
        q=int(input("enter your UTME score:"))
        A = jamb+q
        results=A/2
        if results >=300:
            print(f"congratulations {username} you have been awarded a scholarship")
    else:print(f"sorry {username} unfortunately we are unable to grant you a scholarship  ")





username=input("enter your name:")
print(f"hell0 {username}" )
gender= str(input("enter your sex (male/female):")).lower()
age=int(input("enter your age:"))
if age >= 18:

        nationality=str(input("where are you from:")).lower()
        if nationality=="nigeria":


                print(f"""hello {username} welcome to the princess foundation scholarship 
                we are happy have you 
                to apply for this scholarship fill in the following information""")
                print("enter the grades you scored in your WAEC")
                print("""we offer the following courses
                1.software engineering
                2.medicine
                3.civil engineering
                4.law""")
                department=input("enter the course of your choice:").lower()
                if department=="medicine":
                    a=input("biology:")
                    b=input("chemistry:")
                    c=input("mathematics:")
                    d=input("english:")
                    e=input("physics:")
                    grade_range()
                    jamb_scores()
                elif department=="software engineering":
                    a=input("mathematics:")
                    b=input("english:")
                    c=input("computer science:")
                    d=input("physics:")
                    e=input("chemistry:")
                    grade_range()
                    jamb_scores()
                elif department=="civil engineering":
                    a = input("mathematics:")
                    b = input("english:")
                    c = input("technical drawing:")
                    d = input("physics:")
                    e = input("chemistry:")
                    grade_range()
                    jamb_scores()
                elif department=="law":
                    a = input("mathematics:")
                    b = input("english:")
                    c = input("literature in english:")
                    d = input("government:")
                    e = input("economics:")
                    grade_range()

                    jamb_scores()
                else:print(f"sorry {username} we do not offer scholarship for your course of study")



        else:print("sorry you are not eligible for the scholarship")
        print("thank you")
else: print(f"we are sad to inform you {username } we will not be able to grant you this scholarship")



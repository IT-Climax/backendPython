
def variabes():
    x="princess is a good girl "
    y="she eats food"
    w=x + y
    print(w)
    print("who is princess? " + w)


def for_loop():
    name=("princess ","charity ","joy ")
    dept=("sen","cyb ","csc ")
    age=(11 ,12 ,13)
    for x in name:
        for y in dept:
            for z in age:
                print(x,y,z)
                if x=="charity":
                    break



def to_check_string():
    var=("my name is princess i live in yola nigeria")
    print("yola"in var)
    if "is" in var:
        print("yes there is an adjective in the sentence")
to_check_string()
for_loop()
variabes()




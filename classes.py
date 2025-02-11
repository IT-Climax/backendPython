class FCS:
    def __init__(self,fname,lname,age):
        self.fname=fname
        self.lname=lname
        self.age=age

    def list_of_leaders(self):
        print("this is",self.fname,self.lname,self.age,"years old")
fellowship_leader=FCS ("john","adebayo",18)
assistant_fellowship_leader=FCS("blessing","jacob" ,16)
treasurer=FCS("lisa","james",16)
service_secretary=FCS("catherine","paul",16)
accountant=FCS("ola","adeniyi",17)
librarian=FCS("joy","elijah",15)
choir_leader=FCS("obi","kenneth",16)
fellowship_leader.list_of_leaders()
assistant_fellowship_leader.list_of_leaders()
treasurer.list_of_leaders()
service_secretary.list_of_leaders()
accountant.list_of_leaders()
librarian.list_of_leaders()
choir_leader.list_of_leaders()



class SS3(FCS):
    def __init__(self,fname,lname, position,graduationyear):
        super().__init__(fname, lname, position)
        self.fname=fname
        self.graduationyear=graduationyear
        self.position=position
        print("the student",self.fname,self.lname+" in the position of",self.position +" graduated in the year" ,self.graduationyear)
fellowship_leader=SS3( "john","adebayo","fellowship leader",2018)
assistant_fellowship_leader=SS3("blessing","jacob","assistant fellowship leader",2018)
treasurer=SS3("lisa", "james","treasurer",2018)


class SS2(FCS):
    def __init__(self, fname, lname, position, graduationyear):
        super().__init__(fname, lname, position)
        self.fname = fname
        self.graduationyear = graduationyear
        self.position = position
        print("the student", self.fname, self.lname + " in the position of", self.position + " graduated in the year",
              self.graduationyear)
service_secretary=SS2("catherine","malgwi","service secretary",2019)
accountant=SS2("ola","adeniyi","accountant",2019)



class SS1(FCS):
    def __init__(self, fname, lname, position, graduationyear):
        super().__init__(fname, lname, position)
        self.graduationyear = graduationyear
        self.position = position
        print("the student", self.fname, self.lname + " in the position of", self.position + " graduated in the year",
              self.graduationyear)

librarian=SS1("joy","elijah","librarian",2020)
choir_leader=SS1("obi","kenneth","choir leader",2020)

print("This is the data based of the excos of fcs in the year 2018")





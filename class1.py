class StuDetail:
    def details(self,firstName,lastName,age):
        self.fname=firstName
        self.lname=lastName
        self.fullname=self.fname+" "+self.lname
        self.age=age
ratna=StuDetail()
ratna.details('Ratnakar','CH',25)
print(ratna.fullname,"is",ratna.age," yeas of old")
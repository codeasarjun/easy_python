# multiple inheritance 


class college:
    name="Amrita"

class MCA:
    section="a"

class student(college,MCA):
    def printD(self):
        print(f"college name {self.name} and section in MCA is {self.section}")
s1=student()
s1.printD()
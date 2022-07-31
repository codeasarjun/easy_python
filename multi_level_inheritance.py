# multilevel_inheritance

class college:
    name="amrita"
class dep(college):
    dep_name="Computer Application"

class d(dep):
    cls="MCA"
    def printd(self):
        print(f"College is {self.name}, dep is {self.dep_name} and {self.cls}")


s1=d()
s1.printd()

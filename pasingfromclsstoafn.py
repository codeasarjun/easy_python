# will pass some value from one class function to outside function


class data:
    def __init__(self,d) -> None:
        self.d = d
    def send(self):
        return self.d
    

def f():
    d1=data(20)

    s=d1.send()
    print(s)

f()

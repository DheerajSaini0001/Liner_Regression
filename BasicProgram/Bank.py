class Bank:
    currentamt=0
    def __init__(self,name):
        self.name=name
        print(f"Welcome {name}")
    def Deposite(self,depAmt):
        self.currentamt+=depAmt
        print(f"Your current amount after deopsite of {depAmt} is {self.currentamt} ")
    def Widraw(self,Withdrawamt):
        if(Withdrawamt<self.currentamt):
            self.currentamt-=Withdrawamt
            print(f"Remaining amount is {self.currentamt}")
        else:
            print("Insufficent Balance")
Dheeraj=Bank("Dheeraj")
print(Dheeraj.currentamt)
Dheeraj.Deposite(20000)
print(Dheeraj.currentamt)
Dheeraj.Widraw(2500)
Dheeraj.Widraw(2500)
print(Dheeraj.currentamt)
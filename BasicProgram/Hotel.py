class Hotelbill:
    def __init__(self,name):
        self.name=name
        self.items=[]
        print(f"Welcome {name} sir to RamBagh Jaipur")
    def Additem(self,item_Name,Quantity,Price_Per_Unit):
        Total=Quantity*Price_Per_Unit
        self.items.append(
        {
            "item_name":item_Name,
            "Quantity":Quantity,
            "Price_Per_Unit":Price_Per_Unit,
            "Total_price": Total
        }
          
        )
        
        print(f"{item_Name} added- {Quantity} x {Price_Per_Unit} = {Total}")
    def Bill(self):
        print("="*40)
        print(f"Costumer name - {self.name} Sir")
        print("-"*40)
        amtpayable=0
        for i in self.items:
            print(f"{i['item_name']} -- {i['Quantity']} x {i['Price_Per_Unit']}={i["Total_price"]} ")
            amtpayable+=i["Total_price"]
            
        print("-"*40)
        print(f"Total Amount to Pay: ₹{amtpayable}")
        print("="*40)
        print("Thank you for visiting Hotel Rambagh! 🙏")

Dheeraj=Hotelbill("Dheeraj Saini")
Dheeraj.Additem("Paneer Tikka ",3,200)
Dheeraj.Additem("Allu Tikka ",1,500)
Dheeraj.Additem("Momos ",2,40)
Dheeraj.Additem("Dahi papad ",4,20)
Dheeraj.Bill()
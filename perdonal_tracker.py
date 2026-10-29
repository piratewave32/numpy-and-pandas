
class expenses_tracker():
    
    @staticmethod
    def intro():
        print("Hello Sir/Meddam \n Welcome to Expenses tracker:")
        
        
    def __init__(self):
     self.for_entry = input("Enter yes for starting the Expenses tracker:")
     if self.for_entry =="yes":
              self.record = []
              try:
                self.conclusion = "yes"
                while self.conclusion == "yes":
                 self.date = input("Enter the date :")
                 self.catogory = input("Enter the catagory:")
                 self.ammount = float(input("Enter the expense of today:"))
                 print(f"\nThe total amount of today is{self.ammount} are you conform")
                 self.conclusion = input("Enter yes for starting the Expense tracker:").strip().lower()
                 self.record.append({"Date":self.date,"Catogory":self.catogory,"Amount":self.ammount})
                 with open("expense.csv","a")as file:
                     file.write("Date,Catagory,Amount\n")
                     for row in self.record:

                      file.write(f"{row['Date']},{row['Catogory']},{row['Amount']}\n")
                      
              except ValueError:
                print("enter the valid value")
     else:
        print("Good bye\n Have a Good day")
    
expenses_tracker.intro()
expense = expenses_tracker()
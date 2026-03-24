# objective - the goal is to develop a command line based daily expense tracker that allows user to
#1. add and categorize expenses
#2. view a detailed list of recorded load_expenses
#3. calculate total expenditure
#4. save expenses to a file for persistence across sessions.
#5. delete expenses from a file 

"""scope:
1.expense management:users can add new expenses entries by specifying the item and its cost
2. Expenditure oveerview: users can view a detailed list of all recorded expenses, including item names and their corresponding costs
3. total calculation: the program calculates the total amount spend,ading uses in tracking their overall expenditure
4. data persistence: expenses are saved to a file, allowing users to retain their records across
5. user friendly interface: a simple menu driven interface provides ease of use for inndividuals of all technical levels

fearures:

"""
import os
ex='_Expense Calculator_'
print(ex.center(50))

travelrecord={}
total=0



def view_expense():
      with open("record.txt","r")as file:
          content=file.read()
          print(content)


def calculate_total():
    total = 0
    try:
        with open("record.txt", "r") as file:
            for line in file:
                name, amount = line.strip().split(",")
                total += int(amount)
        print("Total expenditure:", total)
    except FileNotFoundError:
        print("No records found.")
    except ValueError:
        print("Error in record format.")    

def save_exit():
    with open("record.txt", "w") as file:
        for name, amount in travelrecord.items(): 
            file.write(name + "," + str(amount) + "\n")
    print("Saved successfully")           

def delete():
     item = input("Enter item to delete: ")
     try:
         with open("record.txt", "r") as file:
             lines = file.readlines()
         
         # Find and remove the line with the item
         new_lines = []
         deleted = False
         for line in lines:
             name, amount = line.strip().split(",")
             if name.strip() != item.strip():
                 new_lines.append(line)
             else:
                 deleted = True
         
         if deleted:
             with open("record.txt", "w") as file:
                 file.writelines(new_lines)
             print(f"{item} deleted successfully")
             # Also remove from in-memory dict if present
             if item in travelrecord:
                 del travelrecord[item]
         else:
             print(f"Item '{item}' not found in records.")
     except FileNotFoundError:
         print("No record file found.")
     except ValueError:
         print("Error parsing record file.") 

def load_expenses():
    global travelrecord
    try:
        with open("record.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 2:
                    name, amount = parts
                    travelrecord[name] = int(amount)
    except FileNotFoundError:
        pass
    except ValueError:
        print("Error loading some records.")
load_expenses()   

def show():
    print("Option 1: Add Expense")
    print("Option 2: View Expenses")
    print("Option 3: Calculate Total Expense")
    print("Option 4: Save and Exit")
    print("Option 5: Delete Expense")
show()
 

while True:
     choice=int(input("choose a option from 1 to 5 :"))
     if (choice==1) :
          def add_expense(name,amount):
             travelrecord[name]=amount
          name=input("Enter Expense name:")
          amount=int(input("Enter Amount:")) 
          add_expense(name,amount)
     
     elif (choice==2) : 
        view_expense()   
     elif (choice==3) :
        calculate_total()
     elif (choice==4) :
        save_exit()
        break   
     elif (choice==5):
        delete()
     else:
         print("enter valid choice")
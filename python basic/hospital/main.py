import patients                                  
from doctors import add_doctor,get_doctor       
import appointments as apt                      
import billing                              

def main():
    while True:
        print("\n=== HOSPITAL MANAGEMENT SYSTEM ===")
        print("1. Add Patient")
        print("2. Add Doctor")
        print("3. Book Appointment")
        print("4. Generate Bill")
        print("5. Pay Bill")
        print("6. Exit")
        
        choice = input("Enter choice (1-6): ")
        
        if choice == "1":
            pid = input("Enter Patient ID: ")
            name = input("Enter Patient Name: ")
            print(patients.add_patient(pid, name))
            
        elif choice == "2":
            did = input("Enter Doctor ID: ")
            name = input("Enter Doctor Name: ")
            print(add_doctor(did, name))
            
        elif choice == "3":
            aid = input("Enter Appointment ID: ")
            pid = input("Enter Patient ID: ")
            did = input("Enter Doctor ID: ")
            date = input("Enter Date (YYYY-MM-DD): ")
            time = input("Enter Time (e.g. 10:00 AM): ")
            print(apt.add_appointment(aid, pid, did, date, time))
            
        elif choice == "4":
            bid = input("Enter Bill ID: ")
            pid = input("Enter Patient ID: ")
            amount = float(input("Enter Amount: "))
            print(billing.create_bill(bid, pid, amount))
            
        elif choice == "5":
            bid = input("Enter Bill ID: ")
            print(billing.pay_bill(bid))
            
        elif choice == "6":
            print("System closing. Goodbye!")
            break
        else:
            print("Invalid Choice! Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()

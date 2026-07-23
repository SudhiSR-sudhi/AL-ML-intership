
import library.books                                   
from library.members import add_member, get_member      
import library.issue as loan                             
from library import fines                               

def main():
    while True:
        print("\n" + "="*30)
        print(" LIBRARY MANAGEMENT SYSTEM")
        print("="*30)
        print("1. Add New Book")
        print("2. Register New Member")
        print("3. Issue Book to Member")
        print("4. Return Borrowed Book")
        print("5. Charge Overdue Fine")
        print("6. Pay Pending Fine")
        print("7. Exit")
        
        choice = input("\nEnter choice (1-7): ")
        
        if choice == "1":
            bid = input("Enter Book ID: ")
            title = input("Enter Book Title: ")
            print(library.books.add_book(bid, title))
            
        elif choice == "2":
            mid = input("Enter Member ID: ")
            name = input("Enter Member Name: ")
            print(add_member(mid, name))
            
        elif choice == "3":
            iid = input("Enter Transaction Issue ID: ")
            bid = input("Enter Book ID: ")
            mid = input("Enter Member ID: ")
            print(loan.issue_book(iid, bid, mid))
            
        elif choice == "4":
            iid = input("Enter Transaction Issue ID to return: ")
            print(loan.return_book(iid))
            
        elif choice == "5":
            fid = input("Enter Fine ID: ")
            mid = input("Enter Member ID: ")
            amount = float(input("Enter Fine Amount (INR): "))
            print(fines.apply_fine(fid, mid, amount))
            
        elif choice == "6":
            fid = input("Enter Fine ID to clear: ")
            print(fines.pay_fine(fid))
            
        elif choice == "7":
            print("\nShutting down application workspace. Goodbye!")
            break
        else:
            print("Invalid Option! Please select a valid number between 1 and 7.")

if __name__ == "__main__":
    main()

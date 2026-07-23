

issue_data = {}

def issue_book(issue_id, book_id, member_id):
    from library.books import books_data as b_db
    from library.members import members_data as m_db

    if book_id not in b_db:
        return "Error: Book ID does not exist!"
    if member_id not in m_db:
        return "Error: Member ID does not exist!"
    if b_db[book_id]["status"] == "Issued":
        return "Error: This book is already borrowed by someone else!"
        
    # Process loan transaction
    b_db[book_id]["status"] = "Issued"
    issue_data[issue_id] = {"book_id": book_id, "member_id": member_id}
    return "Book issued successfully!"

def return_book(issue_id):
    from library.books import books_data as b_db
    
    if issue_id not in issue_data:
        return "Error: Issue transaction record not found!"
        
    book_id = issue_data[issue_id]["book_id"]
    b_db[book_id]["status"] = "Available"
    del issue_data[issue_id]
    return "Book returned successfully!"

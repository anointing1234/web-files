import sqlite3
import os

# connecting to database
db_directory = r"notepad_program/notepad_data.db"
if not os.path.exists(os.path.dirname(db_directory)):
    os.makedirs(os.path.dirname(db_directory))
storage = sqlite3.connect(db_directory)
cursor = storage.cursor()

def create():
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS NOTEPAD_TABLE(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT NOT NULL,
                Type TEXT NOT NULL,
                Content TEXT NOT NULL,
                Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        storage.commit()
        return True
    except Exception as e:
        print(e)
        return False

def insert(Name, Type, Content, Date=None):
    try:
        columns = ["Name", "Type", "Content", "Date"]
        place_holders = ["?", "?", "?", "?"]
        values = [Name, Type, Content, Date]

        if not Date:
            columns.pop()
            place_holders.pop()
            values.pop()

        sql_query = f"INSERT INTO NOTEPAD_TABLE ({', '.join(columns)}) VALUES ({', '.join(place_holders)})"
        cursor.execute(sql_query, values)
        storage.commit()
        print('Note saved!')
        return True
    except Exception as e:
        print(e)
        return False

def view_all():
    try:
        cursor.execute("SELECT * FROM NOTEPAD_TABLE")
        notes = cursor.fetchall()
        if notes:
            for note in notes:
                print(note)
        else:
            print("No notes found.")
    except Exception as e:
        print(e)

def view_note_by_name_type(name, note_type):
    try:
        cursor.execute("SELECT * FROM NOTEPAD_TABLE WHERE Name=? AND Type=?", (name, note_type))
        notes = cursor.fetchall()
        if notes:
            for note in notes:
                print(note)
        else:
            print("Note not found.")
    except Exception as e:
        print(e)

def delete_note_by_name_type(name, note_type):
    try:
        cursor.execute("DELETE FROM NOTEPAD_TABLE WHERE Name=? AND Type=?", (name, note_type))
        storage.commit()
        print(f"Notes with Name '{name}' and Type '{note_type}' deleted.")
    except Exception as e:
        print(e)

def delete_all_notes():
    try:
        cursor.execute("DELETE FROM NOTEPAD_TABLE")
        storage.commit()
        print("All notes deleted.")
    except Exception as e:
        print(e)

def start_note():
    create()
    while True:
        print("""
            Please select an action:
            1. Create note
            2. Type and insert into notepad
            3. View a note
            4. View all saved notes
            5. Delete a note
            6. Delete all notes
            7. Exit
        """)
        choice = input("Enter choice: ")
        if choice == '1':
            name = input("Enter note name: ")
            note_type = input("Enter note type: ")
            content = input("Enter note content: ")
            insert(name, note_type, content)
        elif choice == '2':
            name = input("Enter note name: ")
            note_type = input("Enter note type: ")
            content = input("Enter note content: ")
            insert(name, note_type, content)
        elif choice == '3':
            name = input("Enter note name: ")
            note_type = input("Enter note type: ")
            view_note_by_name_type(name, note_type)
        elif choice == '4':
            view_all()
        elif choice == '5':
            name = input("Enter note name to delete: ")
            note_type = input("Enter note type to delete: ")
            delete_note_by_name_type(name, note_type)
        elif choice == '6':
            confirm = input("Are you sure you want to delete all notes? (yes/no): ")
            if confirm.lower() == 'yes':
                delete_all_notes()
        elif choice == '7':
            print("Exiting the notepad application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    start_note()

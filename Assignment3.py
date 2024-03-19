import psycopg2


global_conn_params = {
    "dbname": "",
    "user": "",
    "password": "",
    "host": "",
    "port": ""
}

def get_database_connection():
    """Uses global connection parameters to establish a connection to the database."""
    return psycopg2.connect(**global_conn_params)

def getAllStudents():
    """Retrieves and displays all student records."""
    conn = get_database_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM public.students;")
            records = cur.fetchall()
            for record in records:
                print(record)
    finally:
        conn.close()

def addStudent(first_name, last_name, email, enrollment_date):
    """Inserts a new student record into the database."""
    conn = get_database_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO public.students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);",
                        (first_name, last_name, email, enrollment_date))
            conn.commit()
            print(f"Added student: {first_name} {last_name}")
    finally:
        conn.close()

def updateStudentEmail(student_id, new_email):
    """Updates the email address of a specific student."""
    conn = get_database_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("UPDATE public.students SET email = %s WHERE student_id = %s;",
                        (new_email, student_id))
            conn.commit()
            print(f"Updated student ID {student_id} with new email: {new_email}")
    finally:
        conn.close()

def deleteStudent(student_id):
    """Deletes a student record from the database."""
    conn = get_database_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM public.students WHERE student_id = %s;", (student_id,))
            conn.commit()
            print(f"Deleted student ID {student_id}")
    finally:
        conn.close()

if __name__ == "__main__":
    global_conn_params["dbname"] = input("Enter the database name: ")
    global_conn_params["user"] = input("Enter the database user: ")
    global_conn_params["password"] = input("Enter the database password: ")
    global_conn_params["host"] = input("Enter the database host (default 'localhost'): ") or "localhost"
    global_conn_params["port"] = input("Enter the database port (default '5432'): ") or "5432"

    while True:
        print("\nAvailable Actions:")
        print("1. List all students")
        print("2. Add a new student")
        print("3. Update a student's email")
        print("4. Delete a student")
        print("5. Exit")
        choice = input("Choose an action (1-5): ")

        if choice == '1':
            getAllStudents()
        elif choice == '2':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter email: ")
            enrollment_date = input("Enter enrollment date (YYYY-MM-DD): ")
            addStudent(first_name, last_name, email, enrollment_date)
        elif choice == '3':
            student_id = input("Enter student ID to update email: ")
            new_email = input("Enter new email: ")
            updateStudentEmail(student_id, new_email)
        elif choice == '4':
            student_id = input("Enter student ID to delete: ")
            deleteStudent(student_id)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please choose again.")

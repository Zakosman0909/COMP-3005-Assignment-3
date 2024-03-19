# COMP-3005-Assignment-3
Name: Zakariya Osman
Applicant number: 101275379 

# Database Set up
Step 1: Create a PostgreSQL database

Step 2: Create the students table in pgAdmin:

    CREATE TABLE students (
  
      student_id SERIAL PRIMARY KEY,
      
      first_name TEXT NOT NULL,
      
      last_name TEXT NOT NULL,
      
      email TEXT NOT NULL UNIQUE,
      
      enrollment_date DATE
      
      );

Step 3: Insert the intial data:
  INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
  ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
  ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
  ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');


# Running the Code
Step 1: Navagaite to the directory where the code is being stored
Step 2: pip install psycopg2
Step 3: Run the code


# Youtube Video
https://youtu.be/Fb59uPMqCTg

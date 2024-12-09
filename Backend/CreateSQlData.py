import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
connected = sqlite3.connect('test.db')
cursor = connected.cursor()

# Define and execute the CREATE TABLE statement
cursor.execute("""
CREATE TABLE IF NOT EXISTS PATIENT (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME VARCHAR(100) NOT NULL,
    AGE INT NOT NULL,
    GENDER VARCHAR(10) NOT NULL,
    CONDITION VARCHAR(100) NOT NULL,
    ADMITTED_DATE DATE NOT NULL,
    LAB_RESULTS_PENDING BOOLEAN DEFAULT FALSE,
    EMERGENCY_VISIT_TODAY BOOLEAN DEFAULT FALSE
);
""")

# Insert data into the PATIENT table
cursor.execute('''INSERT INTO PATIENT (NAME, AGE, GENDER, CONDITION, ADMITTED_DATE, LAB_RESULTS_PENDING, EMERGENCY_VISIT_TODAY) 
                  VALUES ('John Doe', 45, 'Male', 'Hypertension', '2023-12-01', FALSE, TRUE)''')

cursor.execute('''INSERT INTO PATIENT (NAME, AGE, GENDER, CONDITION, ADMITTED_DATE, LAB_RESULTS_PENDING, EMERGENCY_VISIT_TODAY) 
                  VALUES ('Jane Smith', 34, 'Female', 'Diabetes', '2023-12-02', TRUE, FALSE)''')

cursor.execute('''INSERT INTO PATIENT (NAME, AGE, GENDER, CONDITION, ADMITTED_DATE, LAB_RESULTS_PENDING, EMERGENCY_VISIT_TODAY) 
                  VALUES ('Robert Brown', 60, 'Male', 'Arthritis', '2023-11-29', TRUE, FALSE)''')

cursor.execute('''INSERT INTO PATIENT (NAME, AGE, GENDER, CONDITION, ADMITTED_DATE, LAB_RESULTS_PENDING, EMERGENCY_VISIT_TODAY) 
                  VALUES ('Emily Davis', 28, 'Female', 'Asthma', '2023-12-03', FALSE, TRUE)''')

cursor.execute('''INSERT INTO PATIENT (NAME, AGE, GENDER, CONDITION, ADMITTED_DATE, LAB_RESULTS_PENDING, EMERGENCY_VISIT_TODAY) 
                  VALUES ('Michael Johnson', 50, 'Male', 'Heart Disease', '2023-12-04', TRUE, TRUE)''')

# Fetch and display data from the table
print("Data Inserted in the table:")
data = cursor.execute('''SELECT * FROM PATIENT''')
for row in data:
    print(row)

# Define the function for reading SQL queries
def read_sql_query(LLM_query, cursor):
    try:
        cursor.execute(LLM_query)
        rows = cursor.fetchall()
        print("Query Results:")
        for row in rows:
            print(row)
      
    except sqlite3.Error as e:
        print("Error:", str(e))
        return []
    finally:
        connected.commit()

# Call the function with the required arguments
LLM_query = "SELECT * FROM PATIENT"
read_sql_query(LLM_query, cursor)

# Close the connection
connected.close()

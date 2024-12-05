from dotenv import load_dotenv
load_dotenv()
import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import google.generativeai as genai

# Configure Gemini
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

def clean_sql_query(sql_query):
    """Remove markdown formatting and clean the SQL query"""
    sql_query = sql_query.replace('```sql', '').replace('```', '')
    return sql_query.strip()

def get_gemini_response(question, prompt):
    try:
        response = model.generate_content([prompt[0], question])
        sql_query = response.text.strip()
        return clean_sql_query(sql_query)
    except Exception as e:
        raise Exception(f"Error generating response: {e}")

def execute_query(sql, db_url=None):
    if db_url is None:
        db_url = 'sqlite:///dp.sqlite'
    
    try:
        engine = create_engine(db_url)
        Session = sessionmaker(bind=engine)
        session = Session()
        
        result = session.execute(text(sql))
        
        # Get column names from the result
        columns = result.keys()
        
        # Convert rows to dictionaries with column names as keys
        rows = []
        for row in result.fetchall():
            row_dict = {}
            for idx, column in enumerate(columns):
                row_dict[str(column)] = row[idx]
            rows.append(row_dict)
            
        return rows
    except Exception as e:
        raise Exception(f"SQLAlchemy Error: {e}")
    finally:
        session.close()

prompt = [
    """
    You are an expert at generating SQL queries from natural language questions. The SQL database is named Patient and contains the following columns:
        id: integer, primary key
        name: string, the patient's name
        age: integer, the patient's age
        gender: string, the patient's gender (e.g., 'Male', 'Female')
        condition: string, the medical condition of the patient
        admitted_date: date, the date of admission
        lab_results_pending: boolean, indicates if lab results are pending
        emergency_visit_today: boolean, indicates if the patient visited the emergency room today
    Task:
        Given a natural language question about the patient data, your job is to:
        1. Generate an accurate SQL query to retrieve the required information from the database.
        2. Output the raw SQL query only, without any markdown formatting, backticks, or explanations.
    Rules:
        - Output the bare SQL query only, no markdown, no formatting
        - Do not use ```sql``` tags or any other markdown
        - Ensure the query is syntactically correct for SQLite
        - The query should be on a single line or use simple line breaks
        - Always specify column names explicitly in SELECT statements (avoid SELECT *)
    """
]

class LLM_Data_Controller:
    def __init__(self):
        self.prompt = prompt
    
    def generate_gemini_query(self, user_question):
        return get_gemini_response(user_question, self.prompt)
    
    def execute_query(self, sql):
        return execute_query(sql)
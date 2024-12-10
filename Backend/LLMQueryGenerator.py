from dotenv import load_dotenv
load_dotenv()
import os
import google.generativeai as genai


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

def clean_sql_query(sql_query):
    sql_query = sql_query.replace('```sql', '').replace('```', '')
    return sql_query.strip()

def get_gemini_response(question, prompt):
    try:
        response = model.generate_content([prompt[0], question])
        sql_query = response.text.strip()
        return clean_sql_query(sql_query)
    except Exception as e:
        raise Exception(f"Error generating response: {e}")


prompt = [
    """
   # SQL Query Generation Instructions
## Database Schema
Table: PATIENT
- id: integer (primary key)
- name: string
- age: integer
- gender: string
- condition: string
- admitted_date: date
- lab_results_pending: boolean
- emergency_visit_today: boolean



## Task
Generate an SQL query for a table with the following columns:
- id: integer
- name: string
- age: integer
- gender: string
- condition: string

Ensure the query:
- Returns columns in the order: id, name, age, gender, condition.
- Is compatible with SQLite.
- Includes WHERE clauses as necessary.

Generate an accurate SQL query for natural language questions about patient data.

## Key Guidelines
1. Use explicit column selection (avoid SELECT *)
2. Ensure SQLite compatibility
3. Output raw SQL query only
4. No markdown or additional formatting
5. Use single-line or simple line breaks
6. Include appropriate WHERE, ORDER BY clauses as needed

## Example Queries

### Simple Query
SELECT name, age, condition FROM PATIENT WHERE age > 30;

### Complex Query
SELECT 
    name, 
    age, 
    condition, 
    CASE 
        WHEN lab_results_pending = 1 THEN 'Pending'
        ELSE 'Completed'
    END AS lab_status,
    CASE 
        WHEN emergency_visit_today = 1 THEN 'Yes'
        ELSE 'No'
    END AS emergency_visit,
    STRFTIME('%Y-%m-%d', admitted_date) AS admitted_date,
    DATE('now') AS current_date,
    (JULIANDAY('now') - JULIANDAY(admitted_date)) AS days_admitted
FROM PATIENT
WHERE age > 30 AND lab_results_pending = 1
ORDER BY days_admitted DESC;
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

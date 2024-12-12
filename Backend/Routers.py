import sqlite3
from flask import Blueprint, request, jsonify
from extensions import db
from datetime import datetime
from LLMQueryGenerator import LLM_Data_Controller

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/post/query', methods=['POST'])
def get_data_from_llm():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No input data provided"}), 400
        
        user_question = data.get('question')
        if not user_question:
            return jsonify({"error": "The 'question' field is missing"}), 400
        
        print(f"Received query: {user_question}")
        data_controller = LLM_Data_Controller()
        gemini_query = data_controller.generate_gemini_query(user_question)
        
        from SQLController import execute_query
        connection = sqlite3.connect("test.db")
        cursor = connection.cursor()
        results = execute_query(gemini_query, cursor)
        cursor.close()
        connection.close()
        return jsonify({"query": gemini_query, "results": results}), 200

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return jsonify({"error": str(e)}), 500

# Commented out previous routes for reference
# @user_bp.route('/user', methods=['POST'])
# def add_user():
#     try:
#         data = request.get_json()
#         if not data:
#             return jsonify({"error": "No data provided"}), 400
        
#         # Check if the data is a list or single object
#         if isinstance(data, list):
#             # Handle multiple patients
#             added_patients = []
#             for patient_data in data:
#                 patient = create_patient(patient_data)
#                 added_patients.append(patient)
            
#             db.session.add_all(added_patients)
#             db.session.commit()
#             return jsonify([user_schema.dump(patient) for patient in added_patients]), 201
#         else:
#             # Handle single patient
#             patient = create_patient(data)
#             db.session.add(patient)
#             db.session.commit()
#             return user_schema.jsonify(patient), 201
        
#     except KeyError as e:
#         return jsonify({"error": f"Missing field in request: {str(e)}"}), 400
#     except ValueError as e:
#         return jsonify({"error": f"Invalid data format: {str(e)}"}), 400
#     except Exception as e:
#         db.session.rollback()  # Rollback in case of error
#         return jsonify({"error": str(e)}), 500

# def create_patient(data):
#     admitted_date = datetime.strptime(data['admitted_date'], '%Y-%m-%d').date()
    
#     return Patient(
#         name=data['name'],
#         age=data['age'],
#         gender=data['gender'],
#         condition=data['condition'],
#         admitted_date=admitted_date,
#         lab_results_pending=data['lab_results_pending'] == "Yes",
#         emergency_visit_today=data['emergency_visit_today'] == "Yes"
#     )

# @user_bp.route('/all-patients', methods=['GET'])
# def get_all_patients():
#     try:
#         patients = Patient.query.all()
#         if not patients:
#             return jsonify({"message": "No patients found"}), 404
        
#         all_patients = users_schema.dump(patients)
        
#         return jsonify({"patients": all_patients}), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# Uncomment the following line if you want to test the function directly
# get_data_from_llm()
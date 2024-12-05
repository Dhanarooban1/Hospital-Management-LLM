from flask import Blueprint, request, jsonify
from extensions import db
from CreateSQlData import Patient, user_schema, users_schema
from datetime import datetime
from LLMQueryGenerator import LLM_Data_Controller

user_bp = Blueprint('user_bp', __name__)


@user_bp.route('/user', methods=['POST'])
def add_user():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        admitted_date = datetime.strptime(data['admitted_date'], '%Y-%m-%d').date()
        
        new_patient = Patient(
            name=data['name'],
            age=data['age'],
            gender=data['gender'],
            condition=data['condition'],
            admitted_date=admitted_date,
            lab_results_pending=data['lab_results_pending'] == "Yes",
            emergency_visit_today=data['emergency_visit_today'] == "Yes"
        )
        
        db.session.add(new_patient)
        db.session.commit()
        return user_schema.jsonify(new_patient), 201
    except KeyError as e:
        return jsonify({"error": f"Missing field in request: {str(e)}"}), 400
    except ValueError as e:
        return jsonify({"error": f"Invalid data format: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500





@user_bp.route('/all-patients', methods=['GET'])
def get_all_patients():
    try:
        patients = Patient.query.all()
        if not patients:
            return jsonify({"message": "No patients found"}), 404
        
        all_patients = users_schema.dump(patients)
        
        return jsonify({"patients": all_patients}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@user_bp.route('/post/query', methods=['POST'])
def get_data_from_llm():
    try:
        data = request.json
        user_question = data.get('question')
        print(f"Received query: {user_question}")
        data_controller = LLM_Data_Controller()
        gemini_query = data_controller.generate_gemini_query(user_question)
        result = data_controller.execute_query(gemini_query)
        return jsonify({"result": f"Processing query: {user_question}", "data": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

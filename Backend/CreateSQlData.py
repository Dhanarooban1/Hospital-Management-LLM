from extensions import db, ma

# Database model for Patient
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    condition = db.Column(db.String(100), nullable=False)
    admitted_date = db.Column(db.Date, nullable=False)
    lab_results_pending = db.Column(db.Boolean, default=False)
    emergency_visit_today = db.Column(db.Boolean, default=False)

    def __init__(self, name, age, gender, condition, admitted_date, lab_results_pending, emergency_visit_today):
        self.name = name
        self.age = age
        self.gender = gender
        self.condition = condition
        self.admitted_date = admitted_date
        self.lab_results_pending = lab_results_pending
        self.emergency_visit_today = emergency_visit_today


# Marshmallow schemas for serialization
class PatientSchema(ma.Schema):
    class Meta:
        fields = (
            'id',
            'name',
            'age',
            'gender',
            'condition',
            'admitted_date',
            'lab_results_pending',
            'emergency_visit_today'
        )


user_schema = PatientSchema()
users_schema = PatientSchema(many=True)

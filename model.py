from mongoengine import *


class Patient(Document):
    patient_id = StringField()
    first_name = StringField()
    last_name = StringField()
    gender = StringField()
    age = IntField()
    sex = StringField()

    address = StringField()
    city = StringField()
    state = StringField()
    zip_code = StringField()

    hospital = StringField()

    dob = StringField()
    mrn = StringField()

    is_deceased = BooleanField()
    death_date = StringField()
    dod_ts = StringField()

    last_modified = DateField()


class Treatment(Document):
    treatment_id = StringField(required=True)
    treatment_name = StringField()
    patient_id = StringField()
    active = StringField()
    start_date = DateField()
    end_date = DateField()

    diagnoses = StringField()
    cycles = StringField()
    treatment_line = StringField()


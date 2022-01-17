from core import Transform, Load
from mongo_db_connect import patients_collections, treatments_collections


class Hospital1PatientTransform(Transform):

    def transform(self, row: dict):
        new_row = {
            "patient_id": row.get("\ufeffPatientID"),
            "mrn": row.get("MRN"),
            "patient_dob": row.get("PatientDOB"),
            "is_deceased": row.get("IsDeceased"),
            "dod_ts": row.get("DOD_TS"),
            "last_name": row.get("LastName"),
            "first_name": row.get("FirstName"),
            "gender": row.get("Gender"),
            "sex": row.get("Sex"),
            "address": row.get("Address"),
            "city": row.get("City"),
            "state": row.get("State"),
            "zip_code": row.get("ZipCode"),
            "last_modified_date": row.get("LastModifiedDate"),
        }

        return new_row


class Hospital2PatientTransform(Transform):

    def transform(self, row: dict):
        raise NotImplementedError


class Hospital1TreatmentTransform(Transform):

    def transform(self, row: dict):
        raise NotImplementedError


class Hospital2TreatmentTransform(Transform):

    def transform(self, row: dict):
        raise NotImplementedError


class LoadPatientToMongoDb(Load):
    def load(self, row):
        patients_collections.insert_one(row)


class LoadTreatmentToMongoDb(Load):
    def load(self, row):
        treatments_collections.insert_one(row)

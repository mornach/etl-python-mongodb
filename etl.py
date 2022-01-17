import csv
from _ast import Not
from abc import ABC

from consecution import Node, Pipeline

from mongo_db_connect import db_client, tailor_med_db, patients_collections, treatments_collections


class Transform(Node, ABC):
    def transform(self, row: dict):
        raise NotImplementedError

    def process(self, row):
        transformed = self.transform(row)
        self._push(transformed)


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


class Load(Node, ABC):

    def process(self, row):
        self.load(row)

    def load(self, row: dict):
        raise NotImplementedError


class LoadToMongoDb(Load):
    def load(self, row):
        patients_collections.insert_one(row)


def extract_csv_data(path):
    with open(path, 'r') as data:
        reader = csv.DictReader(data)
        for row in reader:
            yield row


if __name__ == '__main__':
    hospital_1_patient_pipe = Pipeline(
        Hospital1PatientTransform('transform') | LoadToMongoDb('load')
    )

    hospital_1_patient_pipe.consume(extract_csv_data('examples/hospital_1_Patient.csv'))

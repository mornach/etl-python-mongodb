from consecution import Pipeline

from csv_utils import extract_csv_data
from etl import Hospital1PatientTransform, Hospital2PatientTransform, Hospital1TreatmentTransform, \
    Hospital2TreatmentTransform, LoadTreatmentToMongoDb, LoadPatientToMongoDb

if __name__ == '__main__':
    hospital_1_patient_pipe = Pipeline(Hospital1PatientTransform('transform') | LoadPatientToMongoDb('load'))
    hospital_2_patient_pipe = Pipeline(Hospital2PatientTransform('transform') | LoadPatientToMongoDb('load'))

    hospital_1_treatments_pipe = Pipeline(Hospital1TreatmentTransform('transform') | LoadTreatmentToMongoDb('load'))
    hospital_2_treatments_pipe = Pipeline(Hospital2TreatmentTransform('transform') | LoadTreatmentToMongoDb('load'))

    hospital_1_patient_pipe.consume(extract_csv_data('examples/hospital_1_Patient.csv'))
    hospital_1_patient_pipe.consume(extract_csv_data('examples/hospital_2_Patient.csv'))
    hospital_1_patient_pipe.consume(extract_csv_data('examples/hospital_1_Treatment.csv'))
    hospital_1_patient_pipe.consume(extract_csv_data('examples/hospital_2_Treatment.csv'))
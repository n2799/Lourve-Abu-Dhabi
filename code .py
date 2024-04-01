from collections import deque

class Patient:
    def __init__(self, patient_id, name, age, medical_history, current_condition):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.medical_history = medical_history
        self.current_condition = current_condition

    def update_medical_history(self, new_history):
        self.medical_history = new_history

    def update_condition(self, new_condition):
        self.current_condition = new_condition

    def __repr__(self):
        return f"Patient ID: {self.patient_id}, Name: {self.name}, Age: {self.age}, Medical History: {self.medical_history}, Current Condition: {self.current_condition}"

class Prescription:
    def __init__(self, patient_id, medication):
        self.patient_id = patient_id
        self.medication = medication

class Hospital:
    def __init__(self):
        self.patients = []
        self.appointments = []
        self.prescriptions = deque()
        self.consultation_queue = deque()

    def add_patient(self, patient):
        self.patients.append(patient)

    def remove_patient(self, patient_id):
        for patient in self.patients:
            if patient.patient_id == patient_id:
                self.patients.remove(patient)
                print("Patient removed successfully!")
                return True
        print("Patient not found.")
        return False

    def update_patient(self, patient_id, new_medical_history, new_condition):
        for patient in self.patients:
            if patient.patient_id == patient_id:
                patient.update_medical_history(new_medical_history)
                patient.update_condition(new_condition)
                print("Patient record updated successfully!")
                # Update appointments associated with the patient
                for appointment in self.appointments:
                    if appointment["patient_id"] == patient_id:
                        appointment["medical_history"] = new_medical_history
                        appointment["current_condition"] = new_condition
                        print(f"Appointment with Doctor ID {appointment['doctor_id']} on {appointment['appointment_date']} at {appointment['appointment_time']} updated.")
                return
        print("Patient not found.")

    def schedule_appointment(self, patient_id, doctor_id, appointment_date, appointment_time):
        self.appointments.append({"patient_id": patient_id, "doctor_id": doctor_id, "appointment_date": appointment_date, "appointment_time": appointment_time})
        print(f"Appointment scheduled with Doctor ID {doctor_id} on {appointment_date} at {appointment_time} for patient ID {patient_id}")

    def add_prescription(self, prescription):
        self.prescriptions.append(prescription)

    def add_to_consultation_queue(self, patient_id):
        self.consultation_queue.append(patient_id)
        print(f"Patient with ID {patient_id} added to the consultation queue.")

    def consult_next_patient(self):
        if self.consultation_queue:
            next_patient_id = self.consultation_queue.popleft()
            print(f"Consulting patient with ID {next_patient_id}.")
        else:
            print("No patients in the consultation queue.")

    def display_patient_summary(self, patient_id):
        for patient in self.patients:
            if patient.patient_id == patient_id:
                print(patient)
                print("Appointments:")
                for appointment in self.appointments:
                    if appointment["patient_id"] == patient_id:
                        print(f"Doctor ID: {appointment['doctor_id']}, Appointment Date: {appointment['appointment_date']}, Appointment Time: {appointment['appointment_time']}")
                for prescription in self.prescriptions:
                    if prescription.patient_id == patient_id:
                        print(f"Prescription: {prescription.medication}")
                return
        print("Patient not found.")

def main_menu():
    print("\nPatient Record Management System")
    print("1. Add New Patient")
    print("2. Schedule Appointment")
    print("3. Add Prescription")
    print("4. Display Patient Summary")
    print("5. Update Patient Record")
    print("6. Remove Patient")
    print("7. Add to Consultation Queue")
    print("8. Consult Next Patient")
    print("9. Exit")

def add_new_patient(hospital):
    patient_id = int(input("Enter patient ID: "))
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    medical_history = input("Enter medical history: ")
    current_condition = input("Enter current condition: ")
    new_patient = Patient(patient_id, name, age, medical_history, current_condition)
    hospital.add_patient(new_patient)
    print("Patient added successfully!")

def update_patient_record(hospital):

    patient_id = int(input("Enter patient ID: "))
    for patient in hospital.patients:
        if patient.patient_id == patient_id:
            print("Patient found. Please provide the following details to update the record:")
            new_medical_history = input("Enter new medical history: ")
            new_condition = input("Enter new condition: ")
            patient.update_medical_history(new_medical_history)
            patient.update_condition(new_condition)
           
            # Update appointments associated with the patient
            for appointment in hospital.appointments:
                if appointment["patient_id"] == patient_id:
                  
                    doctor_id = int(input("Enter new doctor ID: "))
                    appointment_date = input("Enter new appointment date (YYYY-MM-DD): ")
                    appointment_time = input("Enter new appointment time: ")
                    appointment["doctor_id"] = doctor_id
                    appointment["appointment_date"] = appointment_date
                    appointment["appointment_time"] = appointment_time
                    print("Patient record updated successfully!")
            return
    print("Patient not found.")

def remove_patient(hospital):
    patient_id = int(input("Enter patient ID: "))
    hospital.remove_patient(patient_id)

def schedule_appointment(hospital):
    patient_id = int(input("Enter patient ID: "))
    doctor_id = int(input("Enter doctor ID: "))
    appointment_date = input("Enter appointment date (YYYY-MM-DD): ")
    appointment_time = input("Enter appointment time: ")
    hospital.schedule_appointment(patient_id, doctor_id, appointment_date, appointment_time)
    print("Appointment scheduled successfully!")

def add_prescription(hospital):
    patient_id = int(input("Enter patient ID: "))
    medication = input("Enter prescribed medication: ")
    new_prescription = Prescription(patient_id, medication)
    hospital.add_prescription(new_prescription)
    print("Prescription added successfully!")

def add_to_consultation_queue(hospital):
    patient_id = int(input("Enter patient ID to add to consultation queue: "))
    hospital.add_to_consultation_queue(patient_id)

def consult_next_patient(hospital):
    hospital.consult_next_patient()

def display_patient_summary(hospital):
    patient_id = int(input("Enter patient ID: "))
    hospital.display_patient_summary(patient_id)

def main():
    hospital = Hospital()
    while True:
        main_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_new_patient(hospital)
        elif choice == '2':
            schedule_appointment(hospital)
        elif choice == '3':
            add_prescription(hospital)
        elif choice == '4':
            display_patient_summary(hospital)
        elif choice == '5':
            update_patient_record(hospital)
        elif choice == '6':
            remove_patient(hospital)
        elif choice == '7':
            add_to_consultation_queue(hospital)
        elif choice == '8':
            consult_next_patient(hospital)
        elif choice == '9':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

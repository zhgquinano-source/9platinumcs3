class Patient: # creates the parent class Patient
    def __init__(self, name, bill_amount):
        # Initializes private attributes of the patients
        self.__name = name
        self.__bill_amount = bill_amount

    # Setter methods for title
    def set_name(self, name):
        self.__name = name

    # Setter methods for bill_amount
    def set_bill_amount(self, bill_amount):
        self.__bill_amount = bill_amount

    # Getter methods for name
    def get_name(self):
        return self.__name

    # Getter methods for bill_amount
    def get_bill_amount(self):
        return self.__bill_amount

    # Calculates bill_amount
    def calculate_bill(self):
        return self.__bill_amount

    # method for patient_type
    def display_patient_type(self):
        print("Patient Type: Regular Patient")

class SeniorPatient(Patient): # Creates subclass for senior patient
    def calculate_bill(self):
        return self.get_bill_amount() * 0.80 # Gives the 20% discount for the total bill the patient has to pay

    def display_patient_type(self):
        print("Patient Type: Senior Citizen") # this overrides the parent class patient_type

class PhilHealthPatient(Patient): # Creates subclass for PhilHealth patient
    def calculate_bill(self):
        return self.get_bill_amount() * 0.85 # Gives the 15% discount for the total bill the patient has to pay

    def display_patient_type(self):
        print("Patient Type: PhilHealth Member") # this overrides the previous patient_type

print("Hospital Billing System")
print("------------------------")

patient1 = Patient("Juan Dela Cruz", 15000) # Object for a Patient named "Juan Dela Cruz"
patient2 = SeniorPatient("Maria Santos", 15000) # Object for Senior Patient named "Maria Santos"
patient3 = PhilHealthPatient("Pedro Reyes", 15000) # Object for PhilHealthPatient named "Pedro Reyes"

# creates a list for the loop to work
patients = [patient1, patient2, patient3]

# By using a for loop this Outputs the methods of the Patients one by one 
for patient in patients:
    print(f"Patient Name:  {patient.get_name()}")
    patient.display_patient_type()
    print(f"Original Bill: ₱{patient.get_bill_amount():,.2f}")
    print(f"Final Bill: ₱{patient.calculate_bill():,.2f}\n")

# HIPPO

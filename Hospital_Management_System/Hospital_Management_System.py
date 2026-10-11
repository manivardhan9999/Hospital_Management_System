class Patient:
    def __init__(self, patient_id, name, age, gender, disease):
        self.id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.disease = disease

class HospitalManagementSystem:
    def __init__(self):
        # Using a list to store patient objects
        self.patients = []

    def add_patient(self):
        print("\n--- Add New Patient ---")
        patient_id = input("Enter Patient ID: ").strip()
       
        # Check if ID already exists
        for p in self.patients:
            if p.id == patient_id:
                print("Error: A patient with this ID already exists.")
                return

        name = input("Enter Patient Name: ").strip()
        age = input("Enter Age: ").strip()
        gender = input("Enter Gender: ").strip()
        disease = input("Enter Disease/Ailment: ").strip()

        # Input validation
        if not patient_id or not name:
            print("Error: Patient ID and Name are required fields.")
            return

        # Create object and add to list
        new_patient = Patient(patient_id, name, age, gender, disease)
        self.patients.append(new_patient)
        print(f" Patient '{name}' added successfully!")

    def display_patients(self):
        print("\n--- All Patient Records ---")
        if not self.patients:
            print("No records found in the system.")
            return

        # Header formatting
        print(f"{'ID':<10} | {'Name':<20} | {'Age':<5} | {'Gender':<8} | {'Disease':<20}")
        print("-" * 75)
        for p in self.patients:
            print(f"{p.id:<10} | {p.name:<20} | {p.age:<5} | {p.gender:<8} | {p.disease:<20}")

    def search_patient(self):
        print("\n--- Search Patient ---")
        search_id = input("Enter Patient ID to search: ").strip()
       
        for p in self.patients:
            if p.id == search_id:
                print("\nMatch Found:")
                print(f"🆔 ID: {p.id}")
                print(f"👤 Name: {p.name}")
                print(f"📅 Age: {p.age}")
                print(f"🚻 Gender: {p.gender}")
                print(f"🤒 Disease: {p.disease}")
                return
        print("Patient record not found.")

    def delete_patient(self):
        print("\n--- Delete Patient Record ---")
        delete_id = input("Enter Patient ID to delete: ").strip()
       
        for i, p in enumerate(self.patients):
            if p.id == delete_id:
                removed_patient = self.patients.pop(i)
                print(f"🗑️ Patient '{removed_patient.name}' has been removed successfully.")
                return
        print("Patient ID not found.")

def main():
    hms = HospitalManagementSystem()
   
    while True:
        print("\n==============================")
        print("  HOSPITAL MANAGEMENT SYSTEM  ")
        print("==============================")
        print("1. Add New Patient")
        print("2. View All Patients")
        print("3. Search Patient by ID")
        print("4. Delete Patient Record")
        print("5. Exit")
       
        choice = input("\nEnter your choice (1-5): ").strip()
       
        if choice == '1':
            hms.add_patient()
        elif choice == '2':
            hms.display_patients()
        elif choice == '3':
            hms.search_patient()
        elif choice == '4':
            hms.delete_patient()
        elif choice == '5':
            print("\nThank you for using the Hospital Management System. Goodbye!")
            break
        else:
            print("Invalid selection. Please choose a valid option (1-5).")

if __name__ == "__main__":
    main()

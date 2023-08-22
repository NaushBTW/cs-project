class Patient:
    def __init__(self, age, bp, hr, temp, o2, name, gender, height, weight, bmi):
        self.age = age
        self.bp = bp
        self.hr = hr
        self.temp = temp
        self.o2 = o2
        self.name = name
        self.gender = gender
        self.height = height
        self.weight = weight
        self.bmi = bmi

    def vitals(self):
        print(
            "Patient's name: "
            + self.name
            + "\nPatient's age: "
            + str(self.age)
            + "\nPatient's blood pressure: "
            + str(self.bp)
            + "\nPatient's heart rate: "
            + str(self.hr)
            + "\nPatient's temperature: "
            + str(self.temp)
            + "\nPatient's oxygen level: "
            + str(self.o2)
            + "\nPatient's BMI: "
            + str(self.bmi)
        )

    def info(self):
        print(
            "Patient's name: "
            + self.name
            + "\nPatient's age: "
            + str(self.age)
            + "\nPatient's gender: "
            + str(self.gender)
            + "\nPatient's height: "
            + str(self.height)
            + "\nPatient's weight: "
            + str(self.weight)
        )

    def health_status(self):
        if self.age > 65:
            print("Patient is at high risk")
        elif self.bp > 140:
            print("Patient is at high risk")
        elif self.hr > 100:
            print("Patient is at high risk")
        elif self.temp > 100:
            print("Patient is at high risk")
        elif self.o2 < 90:
            print("Patient is at high risk")
        elif self.bmi > 30:
            print("Patient is at high risk")
        elif self.age > 50:
            print("Patient is at medium risk")
        elif self.bp > 120:
            print("Patient is at medium risk")
        elif self.hr > 90:
            print("Patient is at medium risk")
        elif self.temp > 99:
            print("Patient is at medium risk")
        elif self.o2 < 95:
            print("Patient is at medium risk")
        elif self.bmi > 25:
            print("Patient is at medium risk")
        else:
            print("Patient is at low risk")


def menu():
    print("1. Add a patient")
    print("2. Check patient's health status")
    print("3. Check patient's information")
    print("4. Display all patients in the system")
    print("5. Change patient's information")
    print("6. Delete patient's information")
    print("7. Search for a patient")
    print("8. Filter by details")
    print("9. Display dictionary (for testing purposes)")
    print("10. Exit")
    choice = int(input("Enter your choice: "))
    return choice


def filter_patients(patients, choice):
    if choice == 1:
        print("Filters for age: ")
        print("1. Greater than")
        print("2. Less than")
        print("3. Equal to")
        filter_option = int(input("Enter your choice: "))
        if filter_option == 1:
            age = int(input("Enter age: "))
            for name, patient in patients.items():
                if patient.age > age:
                    print(patient.name)
        elif filter_option == 2:
            age = int(input("Enter age: "))
            for name, patient in patients.items():
                if patient.age < age:
                    print(patient.name)
        elif filter_option == 3:
            age = int(input("Enter age: "))
            for name, patient in patients.items():
                if patient.age == age:
                    print(patient.name)
        else:
            print("Invalid choice")

    elif choice == 2:
        print("Filters for blood pressure: ")
        print("1. Greater than")
        print("2. Less than")
        print("3. Equal to")
        filter_option = int(input("Enter your choice: "))
        if filter_option == 1:
            bp = int(input("Enter blood pressure: "))
            for name, patient in patients.items():
                if patient.bp > bp:
                    print(patient.name)
        elif filter_option == 2:
            bp = int(input("Enter blood pressure: "))
            for name, patient in patients.items():
                if patient.bp < bp:
                    print(patient.name)
        elif filter_option == 3:
            bp = int(input("Enter blood pressure: "))
            for name, patient in patients.items():
                if patient.bp == bp:
                    print(patient.name)
        else:
            print("Invalid choice")

    elif choice == 3:
        print("Filters for heart rate: ")
        print("1. Greater than")
        print("2. Less than")
        print("3. Equal to")
        filter_option = int(input("Enter your choice: "))
        if filter_option == 1:
            hr = int(input("Enter heart rate: "))
            for name, patient in patients.items():
                if patient.hr > hr:
                    print(patient.name)
        elif filter_option == 2:
            hr = int(input("Enter heart rate: "))
            for name, patient in patients.items():
                if patient.hr < hr:
                    print(patient.name)
        elif filter_option == 3:
            hr = int(input("Enter heart rate: "))
            for name, patient in patients.items():
                if patient.hr == hr:
                    print(patient.name)
        else:
            print("Invalid choice")

    elif choice == 4:
        print("Filters for temperature: ")
        print("1. Greater than")
        print("2. Less than")
        print("3. Equal to")
        filter_option = int(input("Enter your choice: "))
        if filter_option == 1:
            temp = int(input("Enter temperature: "))
            for name, patient in patients.items():
                if patient.temp > temp:
                    print(patient.name)
        elif filter_option == 2:
            temp = int(input("Enter temperature: "))
            for name, patient in patients.items():
                if patient.temp < temp:
                    print(patient.name)
        elif filter_option == 3:
            temp = int(input("Enter temperature: "))
            for name, patient in patients.items():
                if patient.temp == temp:
                    print(patient.name)
        else:
            print("Invalid choice")

    elif choice == 5:
        print("Filters for oxygen level: ")
        print("1. Greater than")
        print("2. Less than")
        print("3. Equal to")
        filter_option = int(input("Enter your choice: "))
        if filter_option == 1:
            o2 = int(input("Enter oxygen level: "))
            for name, patient in patients.items():
                if patient.o2 > o2:
                    print(patient.name)
        elif filter_option == 2:
            o2 = int(input("Enter oxygen level: "))
            for name, patient in patients.items():
                if patient.o2 < o2:
                    print(patient.name)
        elif filter_option == 3:
            o2 = int(input("Enter oxygen level: "))
            for name, patient in patients.items():
                if patient.o2 == o2:
                    print(patient.name)
        else:
            print("Invalid choice")

    elif choice == 6:
        print("Filters for BMI: ")
        print("1. Greater than")
        print("2. Less than")
        print("3. Equal to")
        filter_option = int(input("Enter your choice: "))
        if filter_option == 1:
            bmi = int(input("Enter BMI: "))
            for name, patient in patients.items():
                if patient.bmi > bmi:
                    print(patient.name)
        elif filter_option == 2:
            bmi = int(input("Enter BMI: "))
            for name, patient in patients.items():
                if patient.bmi < bmi:
                    print(patient.name)
        elif filter_option == 3:
            bmi = int(input("Enter BMI: "))
            for name, patient in patients.items():
                if patient.bmi == bmi:
                    print(patient.name)
        else:
            print("Invalid choice")

    else:
        print("Invalid choice")


def add_patient(patients):
    name = input("Enter patient's name: ")
    gender = input("Enter patient's gender: ")
    age = int(input("Enter patient's age: "))
    bp = int(input("Enter patient's blood pressure: "))
    hr = int(input("Enter patient's heart rate: "))
    temp = int(input("Enter patient's temperature in fahrenheit: "))
    o2 = int(input("Enter patient's oxygen level: "))
    height = float(input("Enter patient's height in m: "))
    weight = float(input("Enter patient's weight in kg: "))
    bmi = weight / (height * height)
    p = Patient(age, bp, hr, temp, o2, name, gender, height, weight, bmi)
    patients[name] = p


def check_health_status(patients):
    name = input("Enter patient's name: ")
    if name in patients:
        patients[name].vitals()
        patients[name].health_status()
    else:
        print("Patient not found")


def check_patient_info(patients):
    name = input("Enter patient's name: ")
    if name in patients:
        patients[name].info()
    else:
        print("Patient not found")


def display_patients(patients):
    print([name for name in patients])


def change_patient_info(patients):
    print("1. Change patient's name")
    print("2. Change patient's age")
    print("3. Change patient's blood pressure")
    print("4. Change patient's heart rate")
    print("5. Change patient's temperature")
    print("6. Change patient's oxygen level")
    print("7. Change patient's height")
    print("8. Change patient's weight")

    choice = int(input("Enter your choice: "))
    pat_name = input("Enter patient's name: ")

    if pat_name not in patients:
        print("Patient not found")
        return
    if choice == 1:
        new_name = input("Enter patient's new name: ")
        patients[new_name] = patients[pat_name]
        del patients[pat_name]
    elif choice == 2:
        age = int(input("Enter patient's age: "))
        patients[pat_name].age = age
    elif choice == 3:
        bp = int(input("Enter patient's blood pressure: "))
        patients[pat_name].bp = bp
    elif choice == 4:
        hr = int(input("Enter patient's heart rate: "))
        patients[pat_name].hr = hr
    elif choice == 5:
        temp = int(input("Enter patient's temperature in fahrenheit: "))
        patients[pat_name].temp = temp
    elif choice == 6:
        o2 = int(input("Enter patient's oxygen level: "))
        patients[pat_name].o2 = o2
    elif choice == 7:
        height = float(input("Enter patient's height in m: "))
        patients[pat_name].height = height
        bmi = patients[pat_name].weight / (height * height)
        patients[pat_name].bmi = bmi
    elif choice == 8:
        weight = float(input("Enter patient's weight in kg: "))
        patients[pat_name].weight = weight
        bmi = patients[pat_name].weight / (
            patients[pat_name].height * patients[pat_name].height
        )
        patients[pat_name].bmi = bmi
    else:
        print("Invalid choice")


def delete_patient(patients):
    name = input("Enter patient's name: ")
    if name in patients:
        del patients[name]
    else:
        print("Patient not found")


def search_patient(patients):
    name = input("Search: ")
    for i in patients:
        if i.startswith(name):
            print(patients[i].name)
    choice2 = input("Would you like to see a patient's information? (y/n): ")
    if choice2 == "y":
        patient_name = input("Enter patient's name: ")
    else: 
        return
    if patient_name in patients:
        patients[patient_name].info()
    else:
        print("Patient not found")


def main():
    patients = {}
    choice = menu()
    while choice != 10:
        if choice == 1:
            add_patient(patients)
        elif choice == 2:
            check_health_status(patients)
        elif choice == 3:
            check_patient_info(patients)
        elif choice == 4:
            display_patients(patients)
        elif choice == 5:
            change_patient_info(patients)
        elif choice == 6:
            delete_patient(patients)
        elif choice == 7:
            search_patient(patients)
        elif choice == 8:
            print("1. Filter by age")
            print("2. Filter by blood pressure")
            print("3. Filter by heart rate")
            print("4. Filter by temperature")
            print("5. Filter by oxygen level")
            print("6. Filter by BMI")
            filter_choice = int(input("Enter your choice: "))
            filter_patients(patients, filter_choice)
        elif choice == 9:
            print(patients)
        else:
            print("Invalid choice")
        choice = menu()


if __name__ == "__main__":
    main()

class patient:
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
        print("Patient's name: " + self.name + "\nPatient's age: " + str(self.age) + "\nPatient's blood pressure: " + str(self.bp) + "\nPatient's heart rate: " + str(self.hr) + "\nPatient's temperature: " + str(self.temp) + "\nPatient's oxygen level: " + str(self.o2) + "\nPatient's BMI: " + str(self.bmi))
        
    def info(self):
        print("Patient's name: " + self.name + "\nPatient's age: " + str(self.age) + "\nPatient's gender: " + str(self.gender) + "\nPatient's height: " + str(self.height)  + "\nPatient's weight: " + str(self.weight))
        
    def healthstatus(self):
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
    print("9. Display dictionary")
    print("10. Exit")
    choice = int(input("Enter your choice: "))
    return choice


if __name__ == "__main__":
    patients = {}
    choice = menu()
    while choice != 10:
        if choice == 1:
            name = input("Enter patient's name: ")
            gender = input("Enter patient's gender: ")
            age = int(input("Enter patient's age: "))
            bp = int(input("Enter patient's blood pressure: "))
            hr = int(input("Enter patient's heart rate: "))
            temp = int(input("Enter patient's temperature in fahrenheit: "))
            o2 = int(input("Enter patient's oxygen level: "))
            height = float(input("Enter patient's height in m: "))
            weight = float(input("Enter patient's weight in kg: "))
            bmi = weight/(height*height)
            p = patient(age, bp, hr, temp, o2, name, gender, height, weight, bmi)
            patients[name] = p
        elif choice == 2:
            name = input("Enter patient's name: ")
            if name in patients:
                print(patients[name].vitals())
                patients[name].healthstatus()
            else:
                print("Patient not found")
        elif choice == 3:
            name = input("Enter patient's name: ")
            if name in patients:
                print(patients[name].info())
            else:
                print("Patient not found")     
        elif choice == 4:
            print([name for name in patients])     
        elif choice == 5:
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
            
            if name not in patients:
                print("Patient not found")
                continue
            if choice == 1:
                name = input("Enter patient's new name: ")
                patients[pat_name].value = name
                patients[name] = patients[pat_name]
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
                bmi = patients[pat_name].weight/(height*height)
                patients[pat_name].bmi = bmi
            elif choice == 8:
                weight = float(input("Enter patient's weight in kg: "))
                patients[pat_name].weight = weight
                bmi = patients[pat_name].weight/(patients[pat_name].height*patients[pat_name].height)
                patients[pat_name].bmi = bmi
        elif choice == 6:
            name = input("Enter patient's name: ")
            if name in patients:
                del patients[name]
            else:
                print("Patient not found")
        elif choice == 9:
            print(patients)
        else:
            print("Invalid choice")
        choice = menu()
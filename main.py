
class Doctor:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty

class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Appointment:
    def __init__(self, date, patient, doctor):
        self.date = date
        self.patient = patient
        self.doctor = doctor

    def show_appointment(self):
       return (f"Sana: {self.date}.\nBemor: {self.patient.name}, {self.patient.age} yosh.\nShifokor: Dr. {self.doctor.name}, {self.doctor.specialty}.")



doctor_1 = Doctor("Ali", "Dermatolog")
doctor_2 = Doctor("Mir", "Kardiolog")

patient_1 = Patient("Husan", "101")
patient_2 = Patient("Xasan", "16")

appointment_1 = Appointment("2025-05-23", patient_1, doctor_1)
appointment_2 = Appointment("2025-05-24", patient_2, doctor_2)

print(appointment_1.show_appointment())
print()


print(appointment_2.show_appointment())

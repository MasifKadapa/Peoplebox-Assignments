# db/seeds.rb

clinic1 = Clinic.create!(name: "Downtown Health", address: "123 Main St")
clinic2 = Clinic.create!(name: "Eastside Medical", address: "456 East St")

doctor1 = Doctor.create!(name: "Dr. Alice", specialization: "Cardiologist", clinic: clinic1)
doctor2 = Doctor.create!(name: "Dr. Bob", specialization: "Neurologist", clinic: clinic2)

patient1 = Patient.create!(name: "John Doe", age: 30, email: "john@example.com")
patient2 = Patient.create!(name: "Jane Doe", age: 40, email: "jane@example.com")

Appointment.create!(doctor: doctor1, patient: patient1, appointment_date: 2.days.from_now)
Appointment.create!(doctor: doctor2, patient: patient2, appointment_date: 3.days.from_now)


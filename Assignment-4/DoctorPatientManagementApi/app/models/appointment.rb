# app/models/appointment.rb
class Appointment < ApplicationRecord
  # Associations
  belongs_to :doctor
  belongs_to :patient

  # Validations
  validates :date, presence: true
  validates :time, presence: true

  # Additional logic or methods can be added here
end


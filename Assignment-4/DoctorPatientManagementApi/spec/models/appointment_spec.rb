# spec/models/appointment_spec.rb
require 'rails_helper'

RSpec.describe Appointment, type: :model do
  # Test associations
  it { should belong_to(:doctor) }
  it { should belong_to(:patient) }

  # Test validations
  it { should validate_presence_of(:date) }
  it { should validate_presence_of(:time) }

  # Additional tests can be added here
end


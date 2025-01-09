# spec/models/admin_user_spec.rb
require 'rails_helper'

RSpec.describe AdminUser, type: :model do
  # Create a valid admin user for the uniqueness test
  let!(:existing_admin_user) { AdminUser.create!(email: 'admin@example.com', password: 'password123') }

  # Test for case-sensitive uniqueness of the email
  it { should validate_uniqueness_of(:email).case_insensitive }

  # Test for password length validation
  it { should validate_length_of(:password).is_at_least(8) }

  # Additional tests can be added here
end


# app/models/admin_user.rb
class AdminUser < ApplicationRecord
  has_secure_password
  # Validations
  validates :email, presence: true, uniqueness: { case_sensitive: false }
  validates :password, presence: true, length: { minimum: 8 }
  
  # Additional logic or methods can be added here
end


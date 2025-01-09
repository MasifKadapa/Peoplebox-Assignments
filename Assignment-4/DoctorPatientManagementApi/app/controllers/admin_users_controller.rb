class AdminUsersController < ApplicationController
  def create
    admin = AdminUser.new(admin_user_params)
    if admin.save
      render json: { api_key: admin.api_key }, status: :created
    else
      render json: { errors: admin.errors.full_messages }, status: :unprocessable_entity
    end
  end

  private

  def admin_user_params
    params.require(:admin_user).permit(:email, :password, :password_confirmation)
  end
end


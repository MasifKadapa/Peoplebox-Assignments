module Authentication
  extend ActiveSupport::Concern

  included do
    before_action :authenticate_admin
  end

  private

  def authenticate_admin
    api_key = request.headers['Authorization']
    unless AdminUser.exists?(api_key: api_key)
      render json: { error: 'Unauthorized' }, status: :unauthorized
    end
  end
end


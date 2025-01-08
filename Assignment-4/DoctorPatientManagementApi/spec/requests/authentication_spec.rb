# spec/requests/authentication_spec.rb

RSpec.describe "Authentication", type: :request do
  let(:valid_api_key) { 'valid_api_key_here' }
  let(:headers) { { "Authorization" => "Bearer #{valid_api_key}" } }

  describe "GET /appointments" do
    it "returns success with valid API key" do
      # Ensure the controller method is correct (authenticate_admin or authenticate_user)
      get '/appointments', headers: headers
      expect(response).to be_successful
    end
  end
end


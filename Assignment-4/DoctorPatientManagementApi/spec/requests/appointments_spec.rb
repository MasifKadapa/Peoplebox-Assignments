# spec/requests/appointments_spec.rb

RSpec.describe "Appointments", type: :request do
  describe "GET /index" do
    it "returns a successful response" do
      get '/appointments'
      expect(response).to be_successful
    end
  end

  # Additional request tests...
end


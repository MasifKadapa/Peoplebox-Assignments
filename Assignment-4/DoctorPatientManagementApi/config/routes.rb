Rails.application.routes.draw do
  resources :clinics
  resources :doctors
  resources :patients
  resources :appointments
  resources :admin_users, only: [:create]
end


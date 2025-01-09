# db/migrate/xxxxxx_create_appointments.rb
class CreateAppointments < ActiveRecord::Migration[6.0]
  def change
    create_table :appointments do |t|
      t.references :doctor, null: false, foreign_key: true
      t.references :patient, null: false, foreign_key: true
      t.datetime :date, null: false
      t.datetime :time, null: false

      t.timestamps
    end
  end
end


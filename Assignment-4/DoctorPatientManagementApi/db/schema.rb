# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# This file is the source Rails uses to define your schema when running `bin/rails
# db:schema:load`. When creating a new database, `bin/rails db:schema:load` tends to
# be faster and is potentially less error prone than running all of your
# migrations from scratch. Old migrations may fail to apply correctly if those
# migrations use external dependencies or application code.
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema[7.1].define(version: 2025_01_07_185611) do
  # These are extensions that must be enabled in order to support this database
  enable_extension "plpgsql"

  create_table "admin_users", force: :cascade do |t|
    t.string "email", null: false
    t.string "password_digest", null: false
    t.string "api_key", null: false
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "appointments", force: :cascade do |t|
    t.bigint "doctor_id", null: false
    t.bigint "patient_id", null: false
    t.datetime "appointment_date"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["doctor_id"], name: "index_appointments_on_doctor_id"
    t.index ["patient_id"], name: "index_appointments_on_patient_id"
  end

  create_table "clinics", force: :cascade do |t|
    t.string "name"
    t.string "address"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "doctors", force: :cascade do |t|
    t.string "name"
    t.string "specialization"
    t.bigint "clinic_id", null: false
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["clinic_id"], name: "index_doctors_on_clinic_id"
  end

  create_table "patients", force: :cascade do |t|
    t.string "name"
    t.integer "age"
    t.string "email"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["email"], name: "index_patients_on_email", unique: true
  end

  add_foreign_key "appointments", "doctors"
  add_foreign_key "appointments", "patients"
  add_foreign_key "doctors", "clinics"
end

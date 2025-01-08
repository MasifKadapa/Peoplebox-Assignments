# db/migrate/xxxxxx_create_admin_users.rb
class CreateAdminUsers < ActiveRecord::Migration[6.0]
  def change
    create_table :admin_users do |t|
      t.string :email, null: false, default: ""
      t.string :password_digest, null: false, default: ""

      t.timestamps
    end
    add_index :admin_users, :email, unique: true
  end
end


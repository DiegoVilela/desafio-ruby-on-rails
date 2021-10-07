class CreateShops < ActiveRecord::Migration[6.1]
  def change
    create_table :shops do |t|
      t.string :name, limit: 100
      t.string :owner, limit: 100

      t.timestamps
    end
    add_index :shops, :name, unique: true
  end
end

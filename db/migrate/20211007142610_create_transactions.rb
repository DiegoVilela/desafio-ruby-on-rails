class CreateTransactions < ActiveRecord::Migration[6.1]
  def change
    create_table :transactions do |t|
      t.integer :kind
      t.date :date
      t.decimal :value
      t.string :cpf, limit: 11
      t.string :card, limit: 12
      t.time :time
      t.references :shop, null: false, foreign_key: true

      t.timestamps
    end
  end
end

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

ActiveRecord::Schema.define(version: 2021_10_07_142610) do

  create_table "shops", force: :cascade do |t|
    t.string "name", limit: 100
    t.string "owner", limit: 100
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
    t.index ["name"], name: "index_shops_on_name", unique: true
  end

  create_table "transactions", force: :cascade do |t|
    t.integer "kind"
    t.date "date"
    t.decimal "value"
    t.string "cpf", limit: 11
    t.string "card", limit: 12
    t.time "time"
    t.integer "shop_id", null: false
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
    t.index ["shop_id"], name: "index_transactions_on_shop_id"
  end

  add_foreign_key "transactions", "shops"
end

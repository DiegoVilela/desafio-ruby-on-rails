class Shop < ApplicationRecord
  has_many :transactions, dependent: :destroy

  validates :name, presence: true, length: { minimum: 5}, uniqueness: true
  validates :owner, presence: true, length: { minimum: 5}
end

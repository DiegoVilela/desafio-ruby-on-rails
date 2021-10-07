class Shop < ApplicationRecord
  validates :name, presence: true, length: { minimum: 5}, uniqueness: true
  validates :owner, presence: true, length: { minimum: 5}
end

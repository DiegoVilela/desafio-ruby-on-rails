class Transaction < ApplicationRecord
  belongs_to :shop

  validates :kind, numericality: { greater_than: 0, less_than: 10 }, presence: true
  validates :date, :value, :card, :time, presence: true
end

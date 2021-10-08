require "test_helper"

class TransactionTest < ActiveSupport::TestCase
  test "Transactions Exists" do
    assert transactions.length == 2
  end

  test "Accessing transactions of a Shop" do
    assert shops(:rosies_shop).transactions.length == 2
    assert shops(:lucys_shop).transactions.length == 0
  end
end

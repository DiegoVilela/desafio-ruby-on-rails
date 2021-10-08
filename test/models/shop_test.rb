require "test_helper"

class ShopTest < ActiveSupport::TestCase
  test "Rosie's Shop" do
    assert shops(:rosies_shop).name == "Rosie's Shop"
    assert shops(:rosies_shop).owner == "Rosie"
  end

  test "Lucy's Shop" do
    assert shops(:lucys_shop).name == "Lucy's Shop"
    assert shops(:lucys_shop).owner == "Lucy"
  end
end

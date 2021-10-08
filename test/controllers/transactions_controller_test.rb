require "test_helper"

class TransactionsControllerTest < ActionDispatch::IntegrationTest
  test "should create a transaction" do
    s = shops(:rosies_shop)
    post "/shops/#{s.id}/transactions", params: {
      transaction: {
        kind: 9,
        date: Date.current,
        value: 78.21,
        cpf: 12345678910,
        card: "4985****2458",
        time: Time.current,
        shop_id: s.id,
      }
    }
    assert_response :redirect
    follow_redirect!
    assert_response :success
    assert_select "h1", "Rosie's Shop"
    assert_select "h2", "Rosie"
  end

  test "shoul delete a transaction" do
    t = transactions(:one)
    delete "/shops/#{t.shop.id}/transactions/#{t.id}"
    assert_response :redirect
    follow_redirect!
    assert_response :success
    assert_select "td", { count: 0, text: "12345678910" }
    assert_select "td", "10987654321"
  end
end

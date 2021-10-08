require "test_helper"

class ShopsControllerTest < ActionDispatch::IntegrationTest
  test "home page should list all shops and have a link to add a shop" do
    get shops_path
    assert_response :success
    assert_select "h1", "Finance Control"
    assert_select "a", "Rosie's Shop"
    assert_select "a", "Lucy's Shop"
    assert_select "a", "Adicionar Loja"
  end

  test "should create a shop" do
    get new_shop_path
    assert_response :success

    post "/shops", params: { shop: { name: "Shop's Name", owner: 'Fulano' } }
    assert_response :redirect
    follow_redirect!
    assert_response :success
    assert_select "h1", "Shop's Name"
    assert_select "h2", "Fulano"
  end

  test "should edit a shop partially" do
    s = shops(:lucys_shop)
    get shop_path(s)
    assert_response :success

    patch "/shops/#{s.id}", params: { shop: { name: "My Shop" }}
    assert_response :success
  end

  test "should edit a shop" do
    s = shops(:lucys_shop)
    get shop_path(s)
    assert_response :success

    put "/shops/#{s.id}", params: { shop: { name: "My Shop", owner: "John" }}
    assert_response :success
  end

  test "should get destroy" do
    s = shops(:lucys_shop)
    delete "/shops/#{s.id}"
    follow_redirect!
    assert_response :success
    assert_select "h1", "Finance Control"
  end
end

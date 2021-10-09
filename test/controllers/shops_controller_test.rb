require "test_helper"

FIRST_SHOP_NAME = "Rosie's Shop"

class ShopsControllerTest < ActionDispatch::IntegrationTest
  test "home page should list all shops and have a link to add a shop" do
    get shops_path
    assert_response :success
    assert_select "h1", "Finance Control"
    assert_select "a", FIRST_SHOP_NAME
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

  test "should not create a duplicate shop" do
    get new_shop_path
    assert_response :success

    post "/shops", params: { shop: { name: "Rosie's Shop", owner: 'Fulano' } }
    assert_response :success
    assert_select "h1", "Nova Loja"
  end

  test "should edit a shop partially" do
    s = shops(:lucys_shop)
    get edit_shop_path(s.id)
    assert_response :success

    patch "/shops/#{s.id}", params: { shop: { name: "My Shop" }}
    assert_response :success
  end

  test "should edit a shop" do
    s = shops(:lucys_shop)
    put shop_url(s), params: { shop: { name: "My Shop", owner: "New One" } }

    assert_redirected_to shop_path(s)

    s.reload
    assert_equal "My Shop", s.name
    assert_equal "New One", s.owner
  end

  test "should get destroy" do
    s = shops(:lucys_shop)
    delete "/shops/#{s.id}"
    follow_redirect!
    assert_response :success
    assert_select "h1", "Finance Control"
  end

  test "should upload a text file" do
    post handle_upload_path, params: { finance: fixture_file_upload('../../../FINANCEIRO.txt', 'text/plain') }
    follow_redirect!
    assert_response :success
    assert_select "a", "BAR DO JOÃO", 1
    assert_select "a", "LOJA DO Ó - FILIAL", 1
  end
end

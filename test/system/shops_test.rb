require "application_system_test_case"

class ShopsTest < ApplicationSystemTestCase
  test "visiting the index" do
    visit root_path
  
    assert_selector "h1", text: "Finance Control"
    assert_text "Rosie's Shop"
    assert_text "Lucy's Shop"
    assert_text "Adicionar Loja"
  end

  test "showing a shop" do
    visit root_path

    click_on "Rosie's Shop"
    assert_selector "h1", text: "Rosie's Shop"
    assert_selector "h2", text: "Rosie"
  end

  test "editing a shop" do
    s = shops(:rosies_shop)
    visit "/shops/#{s.id}/edit"
    assert_text "Rosie"

    fill_in "Name", with: "John's Shop"
    fill_in "Owner", with: "John"
    click_button
    assert_text "John"
  end
end

class ShopsController < ApplicationController
  def index
    @shops = Shop.all
  end

  def show
    @shop = Shop.find(params[:id])
  end

  def new
    @shop = Shop.new
  end

  def create
    @shop = Shop.new(shop_params)

    if @shop.save
      redirect_to @shop
    else
      render :new
    end
  end

  def edit
  end

  def update
  end

  def destroy
  end

  private
    def shop_params
      params.require(:shop).permit(:name, :owner)
    end
end

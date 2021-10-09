SUBTRACTION_TRANSACTION_TYPES = [2, 3, 9]

class ShopsController < ApplicationController
  def index
    @shops = Shop.all
  end

  def show
    @shop = Shop.find(params[:id])
    @balance = 0
    @shop.transactions.each do |t|
      if SUBTRACTION_TRANSACTION_TYPES.include? t.kind
        @balance -= t.value
      else
        @balance += t.value
      end
    end
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
    @shop = Shop.find(params[:id])
  end

  def update
    @shop = Shop.find(params[:id])

    if @shop.update(shop_params)
      redirect_to @shop
    else
      render :edit
    end
  end

  def destroy
    @shop = Shop.find(params[:id])
    @shop.destroy

    redirect_to root_path
  end

  def handle_line(l)
    kind = l[0,1]

    shop = Shop.find_or_create_by(
      owner: l[48,14].strip,
      name: l[62,19].strip)

    t = Transaction.new
    t.kind = kind
    t.date = Date.strptime(l[1, 8], '%Y%m%d')
    t.value = l[9,10].to_f / 100
    t.cpf = l[19,11]
    t.card = l[30,12]
    t.time = Time.strptime(l[42,6], "%H%M%S")
    t.shop = shop
    t.save
  end

  def handle_upload
    uploaded_file = params[:finance]
    File.foreach(uploaded_file) { |line| handle_line line }

    redirect_to root_path
  end

  private
    def shop_params
      params.require(:shop).permit(:name, :owner)
    end
end

class TransactionsController < ApplicationController
  def create
    @shop = Shop.find(params[:shop_id])
    @transaction = @shop.transactions.create(transaction_params)
    redirect_to shop_path(@shop)
  end

  def destroy
  end

  private
  def transaction_params
    params.require(:transaction).permit(:kind, :date, :value, :cpf, :card, :time)
  end
end

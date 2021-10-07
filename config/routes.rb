Rails.application.routes.draw do
  root 'shops#index'

  resources :shops do
    resources :transactions
  end

  post "/handle-upload", to: "shops#handle_upload"
end

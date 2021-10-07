Rails.application.routes.draw do
  root 'shops#index'

  resources :shops do
    resources :transactions
  end

  get "/upload", to: "shops#upload"
  post "/handle-upload", to: "shops#handle_upload"
end

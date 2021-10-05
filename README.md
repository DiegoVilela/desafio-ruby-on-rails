# Desafio programação - para vaga desenvolvedor Ruby on Rails

Por favor leiam este documento do começo ao fim, com muita atenção.
O intuito deste teste é avaliar seus conhecimentos técnicos, para ser mais específico em Ruby on Rails.
O teste consiste em parsear [este arquivo de texto(FINANCEIRO)](https://github.com/nuticseas/desafio-ruby-on-rails/edit/main/FINANCEIRO.txt) e salvar suas informações(transações financeiras) em uma base de dados a critério do candidato.
Este desafio deve ser feito por você em sua casa. Gaste o tempo que você quiser, porém normalmente você não deve precisar de mais do que algumas horas.

# Instruções de entrega do desafio

1. Primeiro, faça um fork deste projeto para sua conta no Github (crie uma se você não possuir).
2. Em seguida, implemente o projeto tal qual descrito abaixo, em seu clone local.
3. Por fim, envie via email o projeto ou o fork/link do projeto para nutic@seas.ce.gov.br

# Descrição do projeto

Você recebeu um arquivo CNAB com os dados das movimentações finanaceira de várias lojas.
Precisamos criar uma maneira para que estes dados sejam importados para um banco de dados.

Sua tarefa é criar uma interface web que aceite upload do [arquivo FINANCEIRO](https://github.com/nuticseas/desafio-ruby-on-rails/edit/main/FINANCEIRO.txt), normalize os dados e armazene-os em um banco de dados relacional e exiba essas informações em tela.

**Sua aplicação web DEVE:**

1. Ter uma tela (via um formulário) para fazer o upload do arquivo(pontos extras se não usar um popular CSS Framework )
2. Interpretar ("parsear") o arquivo recebido, normalizar os dados, e salvar corretamente a informação em um banco de dados relacional, **se atente as documentações** que estão logo abaixo.
3. Exibir uma lista das operações importadas por lojas, e nesta lista deve conter um totalizador do saldo em conta
4. Ser escrita obrigatoriamente em Ruby 2.0+ e Rails 5+
5. Ser simples de configurar e rodar, funcionando em ambiente compatível com Unix (Linux ou Mac OS X). Ela deve utilizar apenas linguagens e bibliotecas livres ou gratuitas.
6. Git com commits bem descritos
7. PostgreSQL
8. Simplecov para disponibilizar o code coverage
9. Docker compose (Pontos extras se utilizar)
10. Readme file descrevendo bem o projeto e seu setup
11. Incluir informação descrevendo como consumir o endpoint da API

**Sua aplicação web não precisa:**

1. Lidar com autenticação ou autorização (pontos extras se ela fizer, mais pontos extras se a autenticação for feita via OAuth).
2. Ser escrita usando framework Ruby on Rails (mas não há nada errado em usá-los também, use o que achar melhor).
3. Documentação da api.(Será um diferencial e pontos extras se fizer)

# Documentação do FINANCEIRO

| Descrição do campo  | Inicio | Fim | Tamanho | Comentário
| ------------- | ------------- | -----| ---- | ------
| Tipo  | 1  | 1 | 1 | Tipo da transação
| Data  | 2  | 9 | 8 | Data da ocorrência
| Valor | 10 | 19 | 10 | Valor da movimentação. *Obs.* O valor encontrado no arquivo precisa ser divido por cem(valor / 100.00) para normalizá-lo.
| CPF | 20 | 30 | 11 | CPF do beneficiário
| Cartão | 31 | 42 | 12 | Cartão utilizado na transação 
| Hora  | 43 | 48 | 6 | Hora da ocorrência atendendo ao fuso de UTC-3
| Dono da loja | 49 | 62 | 14 | Nome do representante da loja
| Nome loja | 63 | 81 | 19 | Nome da loja

# Documentação sobre os tipos das transações

| Tipo | Descrição | Natureza | Sinal |
| ---- | -------- | --------- | ----- |
| 1 | Débito | Entrada | + |
| 2 | Boleto | Saída | - |
| 3 | Financiamento | Saída | - |
| 4 | Crédito | Entrada | + |
| 5 | Recebimento Empréstimo | Entrada | + |
| 6 | Vendas | Entrada | + |
| 7 | Recebimento TED | Entrada | + |
| 8 | Recebimento DOC | Entrada | + |
| 9 | Aluguel | Saída | - |

# Avaliação

Seu projeto será avaliado de acordo com os seguintes critérios.

1. Sua aplicação preenche os requerimentos básicos?
2. Você documentou a maneira de configurar o ambiente e rodar sua aplicação?
3. Você seguiu as instruções de envio do desafio?
4. Qualidade e cobertura dos testes unitários.

Adicionalmente, tentaremos verificar a sua familiarização com as bibliotecas padrões (standard libs), bem como sua experiência com programação orientada a objetos a partir da estrutura de seu projeto.

Sucesso!

# Solução

## Ambiente de desenvolvimento

1. Clone o repositório do Github e vá para o diretório contendo a solução:
- `git clone git@github.com:DiegoVilela/desafio-ruby-on-rails.git`
- `cd desafio-ruby-on-rails`

2. Faça o checkout para a branch `container`:
- `git checkout container`

3. Inicialize os containers:
- `docker-compose up -d --build`

4. Para executar os testes unitários e ver a porcentagem de cobertura:
- `docker-compose exec web coverage run --source='.' manage.py test`
- `docker-compose exec web coverage report`

5. Acesse o sistema:
- Página inicial: http://localhost:8000/
- Documentação da API: http://localhost:8000/docs
- Visualização do endpoints:
  - Lojas: http://localhost:8000/api/shops
  - Transações: http://localhost:8000/api/transactions

6. (Opcional) Para verificar os logs execute:
- `docker-compose logs -f`

7. Para testar a funcionalidade de upload, pode ser utilizado o arquivo `FINANCEIRO.txt` disponível em `/desafio-ruby-on-rails/code/FINANCEIRO.txt`.

## Ambiente de produção

1. Antes de subir o ambiente de produção, encerre o ambiente de desenvolvimento:
- `docker-compose down -v`

2. Crie os arquivos de configuração no diretório `desafio-ruby-on-rails`:
- `.env.prod`:
```
DEBUG=0
SECRET_KEY=change_me
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=finance_prod
SQL_USER=finance_user
SQL_PASSWORD=finance
SQL_HOST=db
SQL_PORT=5432
DATABASE=postgres
```
- `.env.prod.db`:
```
POSTGRES_USER=finance_user
POSTGRES_PASSWORD=finance
POSTGRES_DB=finance_prod
```

3. Inicie o ambiente de produção:
- `docker-compose -f docker-compose.prod.yml up -d --build`

4. (Opcional) Verifica se os três containers (_nginx_, _web_ e _db_) estão rodando:
- `docker ps`

5. Execute as migrações do banco de dados:
- `docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput`

6. Colete os arquivos estáticos:
- `docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear`

7. Execute os testes unitários:
- `docker-compose -f docker-compose.prod.yml exec web coverage run --source='.' manage.py test`

8. Acesse o sistema:
- Página inicial: http://localhost:1337/
- Documentação da API: http://localhost:1337/docs
- Visualização do endpoints:
  - Lojas: http://localhost:1337/api/shops
  - Transações: http://localhost:1337/api/transactions

## Observações

O ambiente de produção seria apenas para realização testes antes do deploy, onde seria provavelmente utilizado um serviço de banco de
dados gerenciado como o RDS da AWS.

Foi utilizado usuário _root_ nos containers _db_ e _nginx_, o que não é recomendado em
produção.

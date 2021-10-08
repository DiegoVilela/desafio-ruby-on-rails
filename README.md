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

2. Faça checkou para a branch contendo `rails`:
- `git checkout rails`

3. Garantir que o _Webpacker_ encontre `application.js`:
- `bundle exec rake webpacker:install`

4. Inicialize o container do banco de dados:
- `docker run -dp 5432:5432 -e POSTGRES_PASSWORD=1234 -e POSTGRES_USER=finance_user -e POSTGRES_DB=finance_dev postgres`

5. Informe a senha do bando de dados via variável de ambiente do terminal:
- `export FINANCE_PASSWORD="1234"`

6. Execute a migração do banco de dados:
- `bin/rails db:migrate`

7. Execute os testes:
- `bin/rails test:all`

8. Inicialize o servidor local de desenvolvimento:
- `bin/rails server`

9. Acesse o sistema:
- Página inicial: http://localhost:8000/

10. Para testar a funcionalidade de upload, pode ser utilizado o arquivo `FINANCEIRO.txt` disponível em `/desafio-ruby-on-rails/FINANCEIRO.txt`.

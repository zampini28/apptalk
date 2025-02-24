![GitHub license](https://img.shields.io/github/license/jjcapellan/flask-examples-pyjwt.svg)
# Implementação de Criptografia e Autenticação Segura

## Telas
* [ ] Criar tela inicial
* [ ] Criar tela de cadastro de usuário
* [ ] Criar tela de login de usuário
* [ ] Criar tela de contatos
* [ ] Criar tela de conversas

## Banco de Dados
* [ ] Tabela de usuário
* [ ] Tabela de contatos
* [ ] Tabela de sessão
* [ ] Tabela de messagens

## Descrição
* Na tela inicial o usuário poderá ir para fazer cadastro. Ao digitar
  o cadastro, aplicação verificará usuário repetido e enviará um email com
  código. Após a aceitação do código, o usuário poderá efetuar o login.

* No login, a aplicação deverá fazer uma token com duração de um mês. Assim,
  permitindo acesso ao contatos do usuário.

* Ao selecionar um contato, a aplicação deve permitir a visualização das
  conversas do usuário com o contato. 

## Requisitos
* A aplicação deve amazenar o hash da senha. (sal aleatório)
* A aplicação utilizar Token para autentificação.
* A aplicação deve criptografar conversas individuais. (Usando AES & RSA)

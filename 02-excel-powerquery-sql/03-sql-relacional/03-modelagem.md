# 🏗️ Modelagem Relacional e Estrutura de Dados.  

Este documento apresenta os fundamentos da **modelagem relacional**, com foco em organização de dados, integridade e impacto direto na qualidade das consultas SQL.

O objetivo é compreender que **a qualidade da análise começa na estrutura dos dados**.

---

## 🎯 Objetivo do Conteúdo:  

Ao final deste tópico, espera-se que o leitor seja capaz de:

- compreender o que é modelagem relacional;
- identificar entidades e relacionamentos;
- entender o papel da normalização;
- reconhecer problemas de modelagem inadequada;
- avaliar impacto da estrutura nas consultas.

---

# 🧠 O que é Modelagem Relacional?

Modelagem relacional é o processo de **organizar dados em tabelas relacionadas entre si**, de forma estruturada e consistente.

Cada tabela representa uma **entidade** do domínio do problema.

Exemplo:
- clientes;
- pedidos;
- produtos;
- pagamentos.

Essas entidades se relacionam por meio de chaves.

---

# 🔑 Entidades e Relacionamentos:  

## Entidade:  
Representa um objeto ou conceito do mundo real.  

Exemplo:  
- Cliente;  
- Produto;  
- Pedido.  

## Atributos:  
Características da entidade.  

Exemplo:  
- Cliente → id_cliente, nome, email;  
- Produto → id_produto, nome, preco.  

## Relacionamento:  
Conexão entre entidades.  

Exemplo:  
- Um cliente pode ter vários pedidos.  
- Um pedido pode conter vários produtos.  

---

# 🔄 Cardinalidade:  

A cardinalidade define como as entidades se relacionam.   

Principais tipos:   

- 1:1 (um para um)  
- 1:N (um para muitos)  
- N:N (muitos para muitos)  

Entender cardinalidade é essencial para:   
- escrever JOINs corretamente;  
- evitar duplicações inesperadas;  
- interpretar resultados com precisão.   

---

# 📐 Normalização:  

Normalização é o processo de organizar dados para:

- reduzir redundância;
- evitar inconsistências;
- melhorar integridade;
- facilitar manutenção.

---

## 📌 Primeira Forma Normal (1FN):  

- cada célula deve conter apenas um valor;
- não deve haver grupos repetitivos.

---

## 📌 Segunda Forma Normal (2FN):  

- todos os atributos devem depender totalmente da chave primária.

---

## 📌 Terceira Forma Normal (3FN):  

- não deve haver dependências transitivas;
- atributos devem depender apenas da chave primária.

---

# ⚠️ Problemas Comuns de Modelagem:  

Modelagem inadequada pode causar:   

- duplicidade de dados;  
- inconsistência de informações;  
- dificuldade em escrever queries;  
- degradação de desempenho;  
- resultados incorretos em agregações.  

---

# 🧠 Impacto da Modelagem nas Queries:  

Uma modelagem bem feita:  

- simplifica JOINs;  
- reduz necessidade de correções posteriores;  
- evita duplicações inesperadas;   
- melhora legibilidade das consultas.  

Uma modelagem ruim:  

- exige tratamentos complexos;  
- gera resultados inconsistentes;  
- dificulta manutenção.  

---

# 📊 Exemplo Conceitual:  

## Modelo inadequado:  

Tabela vendas:
- id_cliente
- nome_cliente
- id_pedido
- valor
- nome_produto

Problema:
- repetição de informações do cliente;
- redundância;
- risco de inconsistência.

---

## Modelo adequado:  

Tabela clientes:
- id_cliente
- nome_cliente

Tabela pedidos:
- id_pedido
- id_cliente
- valor

Tabela produtos:
- id_produto
- nome_produto

Tabela pedido_produto:
- id_pedido
- id_produto

Esse modelo:
- reduz redundância;
- melhora integridade;
- facilita consultas.

---

# 🔍 Perguntas Antes de Criar ou Avaliar um Modelo:  

- há duplicidade de dados?
- as chaves estão bem definidas?
- os relacionamentos fazem sentido?
- a estrutura facilita consultas futuras?

---

# 📌 Checklist Mental:  

Antes de confiar em um banco de dados:

- [ ] Entendo as entidades envolvidas?
- [ ] Sei identificar a chave primária?
- [ ] Compreendo a cardinalidade?
- [ ] A modelagem favorece integridade?
- [ ] A estrutura facilita análises?

---

# 📌 Consideração Final:  

SQL eficiente começa com modelagem adequada.

Não existe query elegante sobre dados mal estruturados.

Dominar modelagem é compreender que:
- análise depende de estrutura;
- estrutura depende de lógica;
- lógica depende de entendimento do problema.

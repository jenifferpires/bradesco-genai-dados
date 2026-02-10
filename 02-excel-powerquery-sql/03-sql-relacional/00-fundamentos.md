# 🧱 Fundamentos de SQL e Bancos de Dados Relacionais.  

Este documento apresenta os **fundamentos de SQL** e o modelo de **bancos de dados relacionais**, com foco em **entendimento conceitual**, **leitura correta de dados** e **pensamento estruturado** antes da escrita de consultas.

O objetivo não é decorar comandos, mas **compreender como os dados estão organizados e como o SQL opera sobre eles**.

---

## 🎯 Objetivo do Conteúdo:  

Ao final deste tópico, espera-se que o leitor seja capaz de:

- compreender o que é SQL e para que ele é utilizado;
- entender o conceito de banco de dados relacional;
- interpretar tabelas, colunas e registros corretamente;
- pensar em consultas antes de escrevê-las;
- evitar erros conceituais comuns desde o início.

---

## 🧠 O que é SQL?

**SQL (Structured Query Language)** é uma linguagem utilizada para **consultar, manipular e organizar dados** armazenados em bancos de dados relacionais.

Com SQL, é possível:
- recuperar dados (`SELECT`);
- filtrar informações (`WHERE`);
- agrupar resultados (`GROUP BY`);
- relacionar tabelas (`JOIN`);
- criar e manter estruturas de dados.

SQL é uma linguagem **declarativa**: você descreve **o que deseja**, não **como o banco deve executar**.

---

## 🗂️ O que é um Banco de Dados Relacional?

Um banco de dados relacional organiza informações em **tabelas**, compostas por:
- **linhas (registros)**: cada linha representa uma entidade ou ocorrência;
- **colunas (atributos)**: cada coluna representa uma característica dessa entidade.

As tabelas podem ser **relacionadas entre si** por meio de chaves.

---

## 🔑 Chaves e Relacionamentos:  

### Chave Primária (Primary Key):  
- identifica unicamente cada registro de uma tabela;
- não pode ser nula;
- não deve se repetir.

### Chave Estrangeira (Foreign Key):  
- referencia a chave primária de outra tabela;
- estabelece o relacionamento entre tabelas.

Essas chaves garantem **integridade referencial**.

---

## 📐 Pensando em Dados Antes da Query:  

Antes de escrever qualquer consulta SQL, pergunte-se:

- quais tabelas contêm os dados necessários?
- como essas tabelas se relacionam?
- qual o nível de detalhe desejado?
- quais filtros são necessários?
- o resultado deve ser agregado?

Responder a essas perguntas evita consultas incorretas ou ineficientes.

---

## 📊 SQL x Excel: Diferenças Importantes:  

| Excel | SQL |
|------|-----|
| Dados em arquivos | Dados em banco |
| Transformações manuais comuns | Transformações declarativas |
| Alto risco de erro humano | Maior consistência |
| Difícil escalar | Escalável |
| Pouca rastreabilidade | Consultas reproduzíveis |

SQL não substitui o Excel, mas é mais adequado para **dados estruturados e escaláveis**.

---

## ⚠️ Erros Conceituais Comuns:  

- tratar SQL como uma sequência de comandos procedurais;
- escrever consultas sem entender o modelo de dados;
- aplicar filtros sem considerar impacto nos relacionamentos;
- misturar níveis de granularidade.

Esses erros geram resultados incorretos, mesmo com sintaxe válida.

---

## 🧠 Postura Esperada ao Trabalhar com SQL:  

Um bom profissional que utiliza SQL:

- entende o modelo de dados;
- valida resultados com senso crítico;
- escreve consultas legíveis;
- prioriza clareza antes de performance;
- revisa impacto de joins e filtros.

SQL é uma ferramenta de **raciocínio sobre dados**, não apenas de execução.

---

## 📌 Consideração Final:  

Dominar SQL começa por **entender dados e relacionamentos**, não por memorizar comandos.

Uma consulta correta é resultado de:
- boa leitura do problema;
- compreensão do modelo de dados;
- escrita consciente da query.

Sem essa base, consultas podem parecer corretas, mas produzir resultados errados.

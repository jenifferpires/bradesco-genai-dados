# 🔗 SELECT, WHERE e JOINs em SQL.  

Este documento apresenta o uso de `SELECT`, `WHERE` e `JOINs` em SQL, com foco em **leitura correta dos dados**, **impacto na cardinalidade** e **erros conceituais comuns**.

O objetivo não é apenas aprender a sintaxe, mas **entender o efeito real de cada decisão na consulta**.

---

## 🎯 Objetivo do Conteúdo:  

Ao final deste tópico, espera-se que o leitor seja capaz de:

- escrever consultas `SELECT` claras e legíveis;
- aplicar filtros de forma correta;
- compreender o funcionamento de `INNER JOIN` e `LEFT JOIN`;
- identificar impactos de filtros na junção;
- evitar erros clássicos em entrevistas e no dia a dia.

---

## 🧠 SELECT e FROM: a Base da Consulta:  

A estrutura mínima de uma consulta SQL é:

```sql
SELECT coluna1, coluna2
FROM tabela;
```
O `SELECT` define quais colunas serão retornadas.
O `FROM` define de onde os dados vêm.

Evite o uso de `SELECT` * em contextos profissionais, pois:

dificulta leitura;

traz colunas desnecessárias;

pode impactar desempenho;

oculta erros conceituais.

## 🔍 `WHERE`: Filtrando Dados

O `WHERE` é utilizado para filtrar linhas com base em condições.

Exemplo:  
```sql
SELECT *
FROM vendas
WHERE valor > 100;
```
#### ⚠️ Atenção:  
O `WHERE` atua após a definição do conjunto de dados, o que é crucial ao trabalhar com `JOIN`s.

### 🔗 `JOINs`: Relacionando Tabelas.  

`JOINs` permitem combinar dados de múltiplas tabelas com base em uma condição lógica.

### `INNER JOIN`:  

Retorna apenas os registros que possuem correspondência em ambas as tabelas.

```sql
SELECT
    c.id_cliente,
    c.nome,
    p.valor
FROM clientes c
INNER JOIN pedidos p
    ON c.id_cliente = p.id_cliente;
```
Se um cliente não possuir pedidos, ele não aparecerá no resultado.

### `LEFT JOIN`:  

Retorna todos os registros da tabela à esquerda, mesmo quando não há correspondência na tabela à direita.

```sql
SELECT
    c.id_cliente,
    c.nome,
    p.valor
FROM clientes c
LEFT JOIN pedidos p
    ON c.id_cliente = p.id_cliente;
``` 
Clientes sem pedidos aparecerão com valores `NULL` nas colunas de pedidos.

### ⚠️ Erro Clássico: Filtro no `WHERE` após `LEFT JOIN`

Este é um dos erros mais comuns em SQL.

```sql
SELECT *
FROM clientes c
LEFT JOIN pedidos p
    ON c.id_cliente = p.id_cliente
WHERE p.valor > 100;
```
#### ❌ Problema:  
Esse filtro elimina registros `NULL`, fazendo com que o `LEFT JOIN` se comporte como um `INNER JOIN`.

#### ✅ Forma Correta: Filtro no `ON`: 

Quando o filtro faz parte da lógica da junção, ele deve estar no `ON`.

```sql
SELECT *
FROM clientes c
LEFT JOIN pedidos p
    ON c.id_cliente = p.id_cliente
   AND p.valor > 100;
```
Assim:  

todos os clientes são mantidos;  
apenas pedidos acima de 100 são considerados;  
a cardinalidade esperada é preservada.  

## 🧠 Como Pensar JOINs Corretamente?  

Antes de escrever a consulta, pergunte-se:

Quero manter registros mesmo sem correspondência?  
O filtro elimina linhas ou apenas restringe a junção?  
Qual tabela define o conjunto principal de dados?  
O resultado esperado inclui valores nulos?  

Essas perguntas evitam erros silenciosos.  

--- 

### 🧪 Exemplo Comparativo: 

| Situação                               | JOIN       | Filtro |
| -------------------------------------- | ---------- | ------ |
| Manter todos os clientes               | LEFT JOIN  | ON     |
| Apenas clientes com pedidos            | INNER JOIN | WHERE  |
| Restringir pedidos                     | LEFT JOIN  | ON     |
| Eliminar registros sem correspondência | INNER JOIN | WHERE  |

### ⚠️ Outros Erros Comuns:  

Usar LEFT JOIN quando um INNER JOIN seria suficiente;  
Não validar cardinalidade do resultado;  
Misturar filtros de tabelas diferentes no WHERE;  
Confiar no resultado sem validar lógica.  

## 📌 Checklist Mental:  

Antes de finalizar uma query com JOIN:

 Sei qual tabela define o conjunto principal?  

 Entendo o impacto do JOIN escolhido?

 O filtro está no local correto (ON ou WHERE)?

 Validei se o resultado faz sentido?

### 📌 Consideração Final:  

JOINs são um dos pontos mais sensíveis do SQL.  
Uma consulta pode estar sintaticamente correta e ainda assim produzir resultados errados.   

Dominar JOINs é dominar:

leitura de dados;

lógica relacional;

responsabilidade analítica.

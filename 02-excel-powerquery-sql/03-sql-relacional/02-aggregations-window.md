# 📊 Agregações, GROUP BY e Window Functions.  

Este documento aborda o uso de **funções de agregação**, `GROUP BY`, `HAVING` e introduz o conceito de **Window Functions**, fundamentais para análises mais avançadas em SQL.

O foco está em compreender:
- Nível de granularidade;
- Impacto das agregações;
- Diferença entre agrupar e apenas calcular sobre partições;
- Erros conceituais comuns.

---

## 🎯 Objetivo do Conteúdo:  

Ao final deste tópico, espera-se que o leitor seja capaz de:

- Utilizar corretamente funções de agregação;
- Entender a relação entre `SELECT` e `GROUP BY`;
- Diferenciar `WHERE` de `HAVING`;
- Compreender o conceito de window functions;
- Evitar erros clássicos envolvendo granularidade.

---

# 🔢 Funções de Agregação: 

Funções de agregação resumem múltiplas linhas em um único valor.

Principais funções:

- `COUNT()`
- `SUM()`
- `AVG()`
- `MIN()`
- `MAX()`

Exemplo:

```sql
SELECT SUM(valor) AS total_vendas
FROM vendas;

```
Esse comando retorna um único valor: o total de vendas.  

## 🧱 `GROUP BY`: Mudando a Granularidade:  

O `GROUP BY` altera o nível de detalhamento da consulta.

Exemplo:  

```sql 
SELECT
    categoria,
    SUM(valor) AS total_categoria
FROM vendas
GROUP BY categoria;

```

Neste caso:  

Cada categoria passa a representar um grupo;  
O resultado terá uma linha por categoria.  

####  ⚠️ Regra fundamental:
Toda coluna no `SELECT` que não é agregada deve estar no `GROUP BY`.

### ❌ Erro Comum: Misturar Granularidades.  

Exemplo incorreto:    

```sql 
SELECT
    categoria,
    valor,
    SUM(valor)
FROM vendas
GROUP BY categoria;

```

Problema:

`valor` não está agregada;  
`valor` não está no `GROUP BY`;  
A consulta é logicamente inconsistente.  

Esse erro demonstra falta de entendimento de granularidade.

## 🔎 `WHERE` x `HAVING`. 

A diferença entre `WHERE` e `HAVING` é essencial.

`WHERE`:  
Filtra linhas antes da agregação.

```sql
SELECT categoria, SUM(valor)
FROM vendas
WHERE valor > 100
GROUP BY categoria;  

```

`HAVING`:  
Filtra grupos após a agregação.

```sql
SELECT categoria, SUM(valor) AS total
FROM vendas
GROUP BY categoria
HAVING SUM(valor) > 1000;

```  

### ⚠️ Erro comum:  
Usar `WHERE` para filtrar agregações.  

## 🪟 Window Functions (Funções de Janela):  

Window functions permitem realizar cálculos sobre um conjunto de linhas relacionadas, sem alterar a granularidade original da consulta.

Essa é a principal diferença em relação ao `GROUP BY`.

### 📌 Estrutura Geral: 

```sql
FUNCAO() OVER (PARTITION BY coluna ORDER BY coluna)

```

### 🔹 Exemplo 1 — Soma por Categoria sem Agrupar:  

```sql
SELECT
    categoria,
    valor,
    SUM(valor) OVER (PARTITION BY categoria) AS total_categoria
FROM vendas;

```

Resultado:

- mantém todas as linhas;  
- adiciona uma coluna com o total por categoria;  
- não reduz o número de registros.  

### 🔹 Exemplo 2 — Ranking:  

```sql
SELECT
    vendedor,
    valor,
    RANK() OVER (ORDER BY valor DESC) AS ranking
FROM vendas;

```

Window functions são essenciais para:

- rankings;  
- acumulados;  
- médias móveis;  
- comparação entre linhas.  

### ⚠️ Erros Comuns com Window Functions:  

esquecer o OVER();  
confundir PARTITION BY com GROUP BY;  
não definir ORDER BY quando necessário;  
usar window functions sem entender impacto no resultado.  

### 🧠 GROUP BY x Window Function:  

| GROUP BY                | Window Function         |
| ----------------------- | ----------------------- |
| Reduz linhas            | Mantém granularidade    |
| Altera nível de detalhe | Apenas adiciona cálculo |
| Uma linha por grupo     | Uma linha por registro  |
| Agrega dados            | Calcula sobre partições |

Entender essa diferença é crucial em entrevistas técnicas.

### 📌 Checklist Mental:  

Antes de finalizar uma query com agregações:

- Entendo o nível de granularidade da consulta?
- Sei se preciso reduzir linhas ou manter todas?
- O filtro deve estar no WHERE ou HAVING?
- Uma window function resolveria melhor o problema?

### 📌 Consideração Final:  

Agregações e window functions representam um salto na maturidade analítica.

Dominar esses conceitos significa:

- Controlar granularidade;  
- Interpretar resultados corretamente;  
- Evitar erros silenciosos em relatórios e dashboards.  

SQL não é apenas sintaxe.  
É raciocínio estruturado sobre dados.  

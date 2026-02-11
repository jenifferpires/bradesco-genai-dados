# ⚠️ Pegadinhas e Armadilhas em SQL.  

Este documento reúne erros clássicos e armadilhas comuns em SQL, frequentemente exploradas em entrevistas técnicas e também recorrentes no ambiente profissional.

O objetivo é desenvolver **atenção, leitura crítica e responsabilidade analítica**, evitando erros silenciosos que comprometem resultados.

---

## 🎯 Objetivo do Conteúdo:  

Ao final deste tópico, espera-se que o leitor seja capaz de:

- identificar erros conceituais em consultas SQL;
- compreender impactos silenciosos na cardinalidade;
- evitar armadilhas envolvendo filtros e agregações;
- validar resultados com postura crítica.

---

## 🔹 1. `LEFT JOIN` com Filtro no `WHERE`:  

#### Problema:  

```sql
SELECT *
FROM clientes c
LEFT JOIN pedidos p
    ON c.id_cliente = p.id_cliente
WHERE p.valor > 100;
```
#### O que acontece?  
O filtro elimina registros `NULL`, fazendo com que o `LEFT JOIN` se comporte como `INNER JOIN`.

#### Correção:  

```sql
LEFT JOIN pedidos p
    ON c.id_cliente = p.id_cliente
   AND p.valor > 100;
```

## 🔹 2. COUNT(*) x COUNT(coluna):  

#### Problema: 
```sql
SELECT COUNT(coluna)
FROM tabela;
```
Se coluna contém valores NULL, eles não serão contados.

#### Diferença:  

COUNT(*) conta todas as linhas.  
COUNT(coluna) ignora valores NULL.  

Essa diferença pode alterar resultados de forma significativa.

## 🔹 3. `WHERE` x `HAVING`: 

#### Problema:  

```sql
SELECT categoria, SUM(valor)
FROM vendas
WHERE SUM(valor) > 1000
GROUP BY categoria;
```

Erro conceitual: `WHERE` não filtra agregações.

#### Correção:  

```sql
HAVING SUM(valor) > 1000;
```
## 🔹 4. Duplicação por JOIN:  

### Problema:  

`JOIN` em tabela com cardinalidade 1:N pode duplicar registros.

Exemplo:

cliente com múltiplos pedidos;  
soma incorreta se não houver agrupamento adequado.  

### Boa prática:  

verificar cardinalidade;
usar `DISTINCT` apenas quando necessário;
validar contagem antes e depois do `JOIN`.

## 🔹 5. SELECT *  

#### Problema:  

Uso indiscriminado de:

`SELECT *`  

Consequências:  
colunas desnecessárias;
perda de clareza;  
risco de quebra futura caso tabela mude.  

### Boa prática:  

Selecionar apenas colunas necessárias.

## 🔹 6. NULL em Comparações:  

#### Problema:  

```sql
WHERE coluna = NULL
```
Essa comparação nunca será verdadeira.

#### Correção: 
```sql
WHERE coluna IS NULL
```
ou
```sql
WHERE coluna IS NOT NULL
```

## 🔹 7. Mistura de Granularidade:  

#### Problema:  

Misturar dados agregados e não agregados na mesma consulta sem controle.

Exemplo:
```sql
SELECT categoria, valor, SUM(valor)
FROM vendas
GROUP BY categoria;
```
Inconsistência lógica.  

## 🔹 8. Falta de `ORDER BY` em Window Functions:  

Window functions sem ORDER BY podem gerar resultados imprevisíveis.

Sempre que o cálculo depender de sequência, o ORDER BY é obrigatório.

## 🔹 9. Confundir `INNER JOIN` com `LEFT JOIN`:  

Muitos utilizam `LEFT JOIN` por padrão, sem necessidade.

Pergunta essencial:

Preciso manter registros sem correspondência?  

Se não, `INNER JOIN` é mais adequado.

## 🔹 10. Confiar no Resultado Sem Validar:  

Erro silencioso mais perigoso.

Após escrever a query, valide:

número de registros;  
valores agregados;  
presença de duplicações;  
coerência com expectativa do problema.  

### 🧠 Checklist Anti-Erro:  

Antes de finalizar uma query:

-  Entendo a cardinalidade?
-  O filtro está no lugar correto?
-  Validei contagens antes e depois do JOIN?
-  Considerei impacto de NULL?
-  A granularidade está correta?
-  O resultado faz sentido?

### 📌 Consideração Final:  

Grande parte dos erros em SQL não são de sintaxe, mas de lógica e interpretação.  
Uma query pode executar perfeitamente e ainda assim produzir resultado incorreto.  

Maturidade técnica em SQL é demonstrada por:  

validação;  
leitura crítica;  
consciência da estrutura dos dados.  
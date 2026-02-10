# 🧪 Exemplos Práticos — Power Query.  

Este documento apresenta **exemplos práticos de uso do Power Query**, com foco em **transformações comuns**, **organização do fluxo de ETL** e **validação dos dados preparados para análise**.

Os exemplos são conceituais e podem ser reproduzidos com diferentes conjuntos de dados.

---

## 🎯 Objetivo dos Exemplos:  

Os exemplos a seguir têm como objetivos:

- demonstrar transformações frequentes em processos de ETL;
- reforçar boas práticas de preparação de dados;
- mostrar como o Power Query reduz erros manuais;
- preparar dados para uso em Excel, SQL ou outras ferramentas.

---

## 🔹 Exemplo 1 — Limpeza Inicial de Dados:  

### Cenário:  
Uma planilha contém dados de vendas extraídos de diferentes fontes, com:
- colunas desnecessárias;
- linhas vazias;
- formatos inconsistentes.

### Etapas no Power Query:  
- remover colunas irrelevantes;
- excluir linhas vazias ou duplicadas;
- padronizar nomes de colunas;
- ajustar tipos de dados (data, texto, número).

### Validação:  
- verificar se o número de registros faz sentido;
- conferir se os tipos de dados estão corretos;
- garantir que nenhuma informação essencial foi removida.

---

## 🔹 Exemplo 2 — Tratamento de Valores Nulos:  

### Cenário:  
Alguns registros possuem valores ausentes em campos importantes.

### Etapas no Power Query:  
- identificar colunas com valores nulos;
- decidir entre remover registros ou preencher valores;
- aplicar regras consistentes de preenchimento.

### Validação:  
- justificar tecnicamente a decisão tomada;
- verificar impacto da transformação na análise final.

---

## 🔹 Exemplo 3 — Criação de Colunas Derivadas:  

### Cenário:  
Há necessidade de criar informações adicionais a partir de dados existentes.

### Etapas no Power Query:  
- criar coluna de mês e ano a partir de uma data;
- gerar categorias com base em regras;
- padronizar valores textuais.

### Validação:  
- conferir se a lógica aplicada está correta;
- testar com registros diferentes.

---

## 🔹 Exemplo 4 — Mesclagem de Tabelas:  

### Cenário:  
Os dados estão distribuídos em mais de uma tabela, como:
- vendas;
- produtos;
- regiões.

### Etapas no Power Query:  
- definir chave de junção;
- escolher o tipo de junção adequado;
- expandir apenas colunas necessárias.

### Validação:  
- conferir cardinalidade após a junção;
- verificar registros sem correspondência;
- validar se o resultado atende ao objetivo da análise.

---

## 🔹 Exemplo 5 — Atualização Automática:  

### Cenário:  
Os dados são atualizados periodicamente.

### Etapas no Power Query:  
- manter o fluxo de ETL baseado em regras;
- atualizar a fonte de dados;
- executar a atualização automática.

### Validação:  
- verificar se novas entradas são processadas corretamente;
- garantir que regras continuam válidas.

---

## ⚠️ Erros Comuns a Evitar:  

- aplicar transformações sem entender o impacto;
- misturar dados tratados e não tratados;
- renomear consultas de forma genérica;
- ignorar validações após transformações.

---

## 🧠 Boas Práticas Reforçadas:  

- cada etapa deve ter propósito claro;
- transformações devem ser rastreáveis;
- resultados devem ser validados;
- ETL deve ser reproduzível.

---

## 📌 Consideração Final:  

O Power Query é uma ferramenta poderosa para **preparação de dados**, mas seu valor real está na **qualidade do raciocínio aplicado às transformações**.

Automatizar erros não melhora a análise.  
Compreender os dados antes de transformá-los é essencial.

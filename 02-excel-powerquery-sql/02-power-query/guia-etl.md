# 🔄 ETL e Power Query: Preparação de Dados com Consistência.  

Este material apresenta o conceito de **ETL (Extract, Transform, Load)** e o papel do **Power Query** como ferramenta de preparação e transformação de dados no ecossistema do Excel.

O foco está em **reprodutibilidade, rastreabilidade e clareza das transformações**, evitando processos manuais e frágeis.

---

## 🎯 Objetivo do Conteúdo:  

Ao final deste tópico, espera-se que o leitor seja capaz de:

- compreender o conceito de ETL e sua importância;
- identificar quando utilizar Power Query;
- aplicar transformações de dados de forma consistente;
- evitar erros comuns de manipulação manual;
- documentar logicamente o processo de preparação dos dados.

---

## 🧠 O que é ETL?

ETL é o processo de:

- **Extract (Extrair):** obter dados de uma ou mais fontes;
- **Transform (Transformar):** limpar, padronizar e estruturar os dados;
- **Load (Carregar):** disponibilizar os dados prontos para análise.

Esse processo é fundamental para garantir **qualidade e confiabilidade** nas análises.

---

## 📌 Por que Evitar Transformações Manuais?

Transformações manuais em planilhas apresentam riscos significativos, como:

- falta de reprodutibilidade;
- alto risco de erro humano;
- dificuldade de auditoria;
- manutenção complexa.

O Power Query resolve esses problemas ao **registrar cada etapa de transformação** de forma estruturada.

---

## 🛠️ O Papel do Power Query:  

O Power Query é uma ferramenta de **extração e transformação de dados** integrada ao Excel.

Ele permite:
- conectar-se a diferentes fontes de dados;
- aplicar transformações passo a passo;
- atualizar dados automaticamente;
- manter histórico das alterações realizadas.

O Power Query **não substitui o Excel**, mas complementa sua capacidade analítica.

---

## 🔍 Tipos Comuns de Transformações.  

Entre as transformações mais utilizadas estão:

- remoção de linhas e colunas desnecessárias;
- tratamento de valores nulos;
- padronização de formatos (datas, textos, números);
- divisão e mesclagem de colunas;
- criação de colunas calculadas;
- filtragem baseada em regras claras.

Cada transformação deve ter **propósito definido**.

---

## 🧪 Boas Práticas no Uso do Power Query:  

- Comece sempre com dados brutos.
- Evite alterações diretas na planilha final.
- Nomeie consultas de forma clara.
- Revise a ordem das etapas.
- Teste atualizações com novos dados.
- Documente transformações complexas.

Essas práticas garantem análises confiáveis e escaláveis.

---

## ⚠️ Limitações do Power Query.  

Apesar de poderoso, o Power Query possui limitações:

- não substitui bancos de dados em grandes volumes;
- pode apresentar limitações de desempenho;
- não é ideal para lógica extremamente complexa.

Nesses casos, SQL ou Python são alternativas mais adequadas.

---

## 🔄 Integração com SQL e Python.  

O uso do Power Query se integra naturalmente com:

- **SQL**, para consultas e agregações mais complexas;
- **Python**, para automação e análises avançadas.

Entender o papel de cada ferramenta evita sobrecarga e uso inadequado.

---

## 📌 Consideração Final:  

ETL é uma etapa crítica em qualquer análise de dados.

O Power Query permite transformar dados de forma **confiável, documentada e reproduzível**, reduzindo erros e aumentando a qualidade das análises.

Dominar ETL não é saber clicar em opções, mas **entender o impacto de cada transformação aplicada**.

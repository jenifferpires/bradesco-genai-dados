# 🛠️ Técnicas de Prompt Engineering.  

Este documento apresenta **técnicas práticas de Prompt Engineering**, explicando **quando utilizar cada abordagem**, seus benefícios e riscos, além de exemplos comparativos.

O objetivo é aumentar **controle, previsibilidade e qualidade** das respostas geradas por modelos de linguagem.

---

## 🎯 Princípios Antes das Técnicas.  

Antes de aplicar qualquer técnica, valide:

- o objetivo está claro?
- o público-alvo está definido?
- há critérios de qualidade explícitos?
- a resposta pode ser validada?

Sem esses pontos, nenhuma técnica compensará um prompt mal formulado.

---

## 1️⃣ Prompt Direto (Zero-shot).  

### O que é?  
Solicitação direta, sem exemplos prévios.

### Quando usar?   
- tarefas simples;
- explicações conceituais básicas;
- perguntas objetivas.

### Exemplo:  
```text
Explique o que é normalização de dados em SQL.
```

### Riscos:  

- Respostas genéricas;  
- Nível de profundidade imprevisível.  

## 2️⃣ Prompt com Contexto:  

### O que é?  

Prompt que fornece informações adicionais sobre o cenário.

### Quando usar?  

- explicações aplicadas;
- adaptação ao domínio do problema;
- alinhamento com objetivos específicos.

### Exemplo:  

```text
- Estou analisando dados financeiros.  
- Explique normalização de dados em SQL com foco em integridade e performance.  
```

### Benefício:  

- **Respostas mais alinhadas ao contexto real.**

## 3️⃣ Few-shot Prompt (Com Exemplos):  

### O que é?  

Prompt que inclui exemplos de entrada e saída.

### Quando usar?  

- padronização de respostas;
- tarefas repetitivas;
- classificação ou formatação.

### Exemplo:  

```text
Exemplo:
Pergunta: O que é INNER JOIN?
Resposta: INNER JOIN retorna apenas registros com correspondência em ambas as tabelas.

Agora responda:
O que é LEFT JOIN?
```

### Benefício:  

- **maior previsibilidade;**
- **redução de ambiguidades.**

## 4️⃣ Prompt Estruturado por Etapas.  

### O que é?  

Prompt que orienta o modelo a responder seguindo etapas lógicas.

### Quando usar?  

- problemas complexos;
- análises técnicas;
- explicações profundas.

### Exemplo:  
```text
Explique o funcionamento do LEFT JOIN seguindo estas etapas:
1. Definição do conceito.
2. Exemplo simples.
3. Erro comum.
4. Boa prática.
```

### Benefício:  

- **respostas organizadas;**
- **fácil validação.**

## 5️⃣ Prompt com Restrições Explícitas.  

### O que é?  

Prompt que define claramente o que não deve ser feito.

### Quando usar?  

- evitar jargões;
- limitar escopo;
- controlar formato da resposta.

### Exemplo:  
```text
Explique JOIN em SQL.
Não utilize termos avançados.
Não inclua subqueries.
Use apenas um exemplo simples.
```

### Benefício:  

- **redução de ruído;**    
- **foco no essencial.**   

## 6️⃣ Prompt Orientado a Validação.  

### O que é?  

Prompt que solicita verificação ou revisão da própria resposta.

### Quando usar?  

- conteúdos críticos;  
- revisões técnicas;  
- identificação de erros.  

Exemplo:
```text
Explique LEFT JOIN.
Em seguida, liste possíveis erros na explicação e corrija-os.
```

### Benefício:  

- **aumento da confiabilidade;** 
- **incentivo à autocrítica do modelo.**

## ⚠️ Técnicas que Exigem Cuidado:  

**Cadeia de Pensamento Explícita**

Solicitar raciocínio passo a passo pode:
- ajudar no entendimento;
- expor raciocínios incorretos;
- gerar excesso de texto.

Utilize apenas quando necessário e sempre valide.

## 🔍 Como Escolher a Técnica Adequada?  

Pergunte-se:

- a tarefa é simples ou complexa?
- preciso de padronização?
- há risco de ambiguidade?
- a resposta será reutilizada?

A técnica deve servir ao objetivo, não o contrário.

## 📌 Boas Práticas Gerais:  

- Combine técnicas quando necessário.
- Prefira clareza a complexidade.
- Documente prompts reutilizáveis.
- Revise e refine continuamente.
- Nunca abdique da validação humana.

## 📌 Consideração Final:  

Técnicas de Prompt Engineering são ferramentas de controle, não garantias de acerto.

O domínio real está em:

- formular bons problemas;
- interpretar respostas criticamente;
- ajustar abordagens conforme o contexto.

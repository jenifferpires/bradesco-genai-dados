# 🧩 Guia de Prompt Engineering

Este documento apresenta os fundamentos de **Prompt Engineering**, com foco em **clareza, controle e previsibilidade** das respostas geradas por modelos de linguagem.

O objetivo é capacitar o uso consciente da IA Generativa, evitando dependência, ambiguidades e resultados inconsistentes.

---

## 📌 O que é Prompt Engineering?

Prompt Engineering é o conjunto de técnicas utilizadas para **estruturar a entrada (prompt)** fornecida a um modelo de linguagem, de modo a orientar a geração de respostas mais relevantes, consistentes e alinhadas ao objetivo desejado.

Prompt Engineering **não substitui conhecimento técnico**.  
Ele potencializa a interação com o modelo quando o objetivo está bem definido.

---

## 🎯 Objetivos de um Bom Prompt

Um bom prompt deve:

- definir claramente o objetivo da tarefa;
- fornecer contexto suficiente, sem excesso;
- estabelecer restrições e critérios de qualidade;
- reduzir ambiguidades;
- facilitar a validação da resposta.

---

## 🧠 Estrutura Recomendada de um Prompt

Sempre que possível, utilize a seguinte estrutura:

1. **Contexto**  
   Explique o cenário no qual a tarefa está inserida.

2. **Objetivo**  
   Deixe claro o que se espera como resultado.

3. **Instruções**  
   Defina como a resposta deve ser construída.

4. **Restrições**  
   Limite escopo, formato ou abordagem.

5. **Critérios de Qualidade**  
   Indique o que caracteriza uma boa resposta.

---

## ❌ Exemplo de Prompt Ruim: 

```text
Explique SQL.
```

Problemas deste prompt:

- objetivo vago;
- ausência de contexto;
- nível de detalhe indefinido;
- resposta imprevisível.

## ✅ Exemplo de Prompt Melhorado:

```text 
Explique o conceito de JOIN em SQL para uma pessoa iniciante.
Utilize exemplos simples.
Destaque diferenças entre INNER JOIN e LEFT JOIN.
Evite jargões sem explicação.
```

Por que este prompt é melhor:

- define público-alvo;
- delimita o escopo;
- orienta a forma da resposta;
- facilita validação.

## 🧪 Prompt com Estrutura Completa:  

```text
Contexto:
Estou estudando SQL aplicado à análise de dados.

Objetivo:
Quero entender como o LEFT JOIN funciona.

Instruções:
Explique o conceito de LEFT JOIN.
Apresente um exemplo simples em SQL.
Mostre um erro comum envolvendo filtros no WHERE.

Restrições:
Não utilize exemplos excessivamente complexos.

Critérios de qualidade:
A explicação deve ser clara e adequada para iniciantes.
```

**Esse formato reduz significativamente respostas genéricas.**

## ⚠️ Erros Comuns em Prompt Engineering:  

- prompts excessivamente longos e confusos;  
- múltiplos objetivos no mesmo prompt;  
- ausência de critérios de validação;  
- dependência cega da resposta gerada;  
- falta de revisão crítica.  

## 🔍 Validação da Resposta:  

Após receber uma resposta gerada por IA, sempre:

- verifique a correção conceitual;
- valide exemplos apresentados;
- confronte com fontes confiáveis;
- ajuste o prompt, se necessário.

**Prompt Engineering é um processo iterativo.**

## 📌 Boas Práticas:  

- Comece simples e refine progressivamente.
- Seja explícito sobre o que não deseja.
- Utilize exemplos quando possível.
- Prefira prompts estruturados em tarefas críticas.
- Documente prompts reutilizáveis.

## 📌 Consideração Final:  

Prompt Engineering é uma habilidade de comunicação técnica, não um truque.

A qualidade da interação com a IA depende diretamente da clareza do pensamento humano que a orienta.

Dominar prompts é dominar a capacidade de formular problemas com precisão.



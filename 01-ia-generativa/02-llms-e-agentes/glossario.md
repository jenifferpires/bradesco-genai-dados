# 📖 Glossário — LLMs e Agentes.  

Este glossário reúne os **principais termos técnicos** utilizados no contexto de **Modelos de Linguagem de Grande Escala (LLMs)** e **Agentes** ao longo deste módulo.

O objetivo é garantir **consistência de linguagem**, **clareza conceitual** e **redução de ambiguidades** em todo o repositório.

Sempre que um termo for utilizado com significado específico, ele deve estar alinhado às definições apresentadas aqui.

---

## 🔤 Termos e Definições:  

### Modelo de Linguagem (Language Model).  
Sistema de Inteligência Artificial treinado para prever a próxima palavra (ou token) em uma sequência de texto, com base em padrões estatísticos aprendidos a partir de dados.

---

### Modelo de Linguagem de Grande Escala (LLM).  
Modelo de linguagem treinado com grandes volumes de dados e parâmetros, capaz de gerar texto coerente, responder perguntas e auxiliar em tarefas linguísticas diversas.

Apesar da complexidade, um LLM **não possui compreensão real**, apenas calcula probabilidades.

---

### Token:  
Unidade básica de texto utilizada por modelos de linguagem.

Um token pode representar:
- uma palavra inteira;
- parte de uma palavra;
- um caractere ou símbolo.

A tokenização influencia diretamente custo, desempenho e qualidade das respostas.

---

### Tokenização:  
Processo de conversão de texto em tokens, que serão processados pelo modelo.

Diferentes modelos utilizam estratégias diferentes de tokenização.

---

### Prompt:  
Entrada fornecida ao modelo de linguagem para orientar a geração de respostas.

Um prompt pode conter:
- instruções;
- contexto;
- exemplos;
- restrições.

A qualidade do prompt influencia diretamente o resultado.

---

### Prompt Engineering:  
Conjunto de técnicas utilizadas para estruturar prompts de forma clara, precisa e eficiente, visando obter respostas mais relevantes e confiáveis.

Não substitui conhecimento técnico, mas potencializa o uso do modelo.

---

### Alucinação:  
Comportamento no qual o modelo gera informações incorretas, inventadas ou não verificáveis, apresentadas com alta confiança.

Esse fenômeno reforça a necessidade de validação humana.

---

### Agente:  
Sistema que utiliza um modelo de linguagem como parte de um fluxo maior de decisão, podendo executar múltiplas etapas, interagir com ferramentas e manter estado entre ações.

Um agente combina:
- modelo de linguagem;
- lógica de controle;
- integração com ferramentas externas.

---

### Ferramentas (Tools).  
Recursos externos acessados por agentes, como:
- APIs;
- bancos de dados;
- sistemas internos;
- funções de código.

Ferramentas ampliam a capacidade de ação do agente além da geração de texto.

---

### Contexto:  
Conjunto de informações fornecidas ao modelo para orientar suas respostas.

Pode incluir:
- histórico da conversa;
- dados adicionais;
- regras ou restrições.

Contexto excessivo ou mal estruturado pode degradar a resposta.

---

### Janela de Contexto:  
Limite máximo de tokens que um modelo consegue considerar simultaneamente.

Quando o limite é excedido, informações antigas podem ser descartadas.

---

### Validação Humana:  
Processo de verificação, revisão e confirmação das respostas geradas por IA por um profissional responsável.

A validação humana é obrigatória em qualquer uso profissional de IA.

---

## 📌 Consideração Final:  

O uso consistente destes termos ao longo do repositório é fundamental para:
- manter clareza conceitual;
- facilitar revisões futuras;
- apoiar treinamento e onboarding.

Sempre que um novo termo relevante surgir, este glossário deve ser atualizado.

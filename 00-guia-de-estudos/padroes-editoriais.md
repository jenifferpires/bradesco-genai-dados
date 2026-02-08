# 📘 Padrões Editoriais do Repositório.  

Este documento define os **padrões oficiais de escrita, organização e apresentação de conteúdo** adotados neste repositório.

Seu objetivo é garantir que todo o material aqui produzido seja:
- tecnicamente correto;
- didático e acessível;
- consistente em estilo e linguagem;
- adequado para estudo individual, treinamento de equipes e validação de conhecimento profissional.

Este não é apenas um repositório de estudos, mas um **guia técnico de referência**, que deve refletir boas práticas de documentação utilizadas em ambientes corporativos e educacionais.

---

## 1. Princípios Fundamentais:  

Todo conteúdo criado neste repositório deve obedecer aos seguintes princípios.

### 1.1 Clareza
- Cada conceito deve ser explicado de forma direta e objetiva.
- Evitar frases longas ou ambíguas.
- Uma ideia principal por parágrafo.

### 1.2 Precisão Técnica
- Nenhuma afirmação deve ser vaga ou genérica.
- Sempre que possível, indicar **condições, limitações e exceções**.
- Diferenciar claramente comportamento esperado de comportamento indesejado.

### 1.3 Didática Progressiva
O conteúdo deve evoluir do simples para o complexo, respeitando diferentes níveis de conhecimento.

Sempre que possível, seguir a ordem:
1. O que é.
2. Para que serve.
3. Como funciona.
4. Exemplo simples.
5. Exemplo aplicado ao mundo real.
6. Erros comuns e pegadinhas.
7. Boas práticas.
8. Checklist mental.

### 1.4 Escrita Profissional
O texto deve ser adequado para:
- documentação técnica;
- material de treinamento;
- onboarding de novos membros;
- revisão de conceitos por profissionais experientes.

Não assumir conhecimento prévio do leitor.

---

## 2. Linguagem e Tom:  

### 2.1 Idioma
- Todo o conteúdo deve ser escrito em **português**.
- Utilizar português técnico, claro e formal.
- Evitar gírias, abreviações informais ou linguagem coloquial.

### 2.2 Tom
- Neutro, técnico e instrutivo.
- Evitar opiniões pessoais sem fundamentação.
- Quando houver recomendação, justificar o motivo.

❌ Incorreto:
> Normalmente isso dá problema.

✅ Correto:
> Esse comportamento pode gerar inconsistências nos resultados, especialmente em cenários com dados incompletos.

---

## 3. Pontuação e Estrutura de Frases:  

A pontuação correta é obrigatória e faz parte da qualidade técnica do material.

### 3.1 Regras Gerais
- Frases devem terminar com ponto final.
- Usar dois pontos para introduzir listas, explicações ou exemplos.
- Usar ponto e vírgula apenas quando necessário para separar ideias relacionadas.
- Usar ponto de interrogação apenas em perguntas reais.

### 3.2 Frases Curtas e Objetivas
- Priorizar frases curtas e diretas.
- Evitar parágrafos longos (máximo recomendado: 4 linhas).

❌ Incorreto:
> O LEFT JOIN quando filtrado no WHERE pode acabar se comportando como INNER JOIN e isso pode causar erros difíceis de perceber.

✅ Correto:
> O `LEFT JOIN`, quando filtrado no `WHERE`, pode se comportar como um `INNER JOIN`.  
> Isso ocorre porque os registros nulos são eliminados pelo filtro.

---

## 4. Estrutura dos Arquivos Markdown:  

Todo arquivo `.md` deve seguir uma estrutura lógica e previsível.

### 4.1 Estrutura Recomendada
Sempre que aplicável, utilizar as seguintes seções:

- Título principal
- Objetivo
- Conceitos fundamentais
- Funcionamento
- Exemplos
- Erros comuns e pegadinhas
- Boas práticas
- Checklist mental
- Referências

Nem todas as seções são obrigatórias, mas a ausência deve ser justificada pelo contexto.

---

## 5. Uso de Títulos e Hierarquia:  

### 5.1 Títulos
- Usar `#` apenas para o título principal do arquivo.
- Usar `##` para seções.
- Usar `###` para subseções.
- Evitar pular níveis de hierarquia.

### 5.2 Emojis
- Permitidos apenas em títulos principais.
- Usar com moderação.
- Nunca usar emojis no corpo do texto técnico.

---

## 6. Ênfase, Alertas e Destaques:  

### 6.1 Ênfase
- Utilizar **negrito** para destacar conceitos-chave.
- Evitar uso excessivo de itálico.

### 6.2 Alertas
Utilizar blockquotes para alertas importantes.

Exemplos:

> ⚠️ **Atenção:**  
> Este comportamento pode alterar a cardinalidade do resultado.

> ✅ **Boa prática:**  
> Sempre validar o resultado após aplicar filtros em junções.

> 💡 **Dica:**  
> Prefira aplicar filtros relacionados à junção diretamente no `ON`.

---

## 7. Blocos de Código:  

### 7.1 Regras
- Todo bloco de código deve estar corretamente formatado.
- Sempre que possível, comentar o código.
- Indicar a linguagem do bloco (ex: `sql`, `python`).

### 7.2 Exemplos
- Primeiro: exemplo simples.
- Depois: exemplo aplicado ao contexto profissional.

Evitar exemplos irreais ou excessivamente simplificados.

---

## 8. Listas e Tabelas:  

### 8.1 Listas
- Sempre introduzir listas com uma frase explicativa.
- Evitar listas sem contexto.

### 8.2 Tabelas
Utilizar tabelas quando houver comparação entre conceitos.

Exemplo:
- INNER JOIN vs LEFT JOIN
- Prompt bom vs prompt ruim
- Boa prática vs erro comum

---

## 9. Referências e Fontes:  

- Sempre que possível, incluir referências.
- Priorizar documentação oficial.
- Indicar claramente quando algo é baseado em experiência prática.

Exemplo:
> Referência: Documentação oficial do PostgreSQL.

---

## 10. Padronização entre Arquivos:  

- A terminologia deve ser consistente em todo o repositório.
- Se um conceito foi definido em um módulo, manter a mesma definição nos demais.
- Evitar sinônimos técnicos que possam gerar ambiguidade.

---

## 11. Responsabilidade do Conteúdo:  

Todo conteúdo inserido neste repositório deve:
- ser revisado antes do commit;
- respeitar estes padrões editoriais;
- contribuir para a qualidade geral do material.

Este documento deve ser tratado como **referência obrigatória** durante toda a evolução do repositório.

---

📌 **Este repositório representa aprendizado contínuo, prática profissional e compromisso com a excelência técnica.**

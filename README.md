# 🐷 Torcedor Palmeiras Bot

## 📒 Descrição
Este é um bot do Telegram que imita um torcedor fanático do Palmeiras, pronto para defender o clube com fervor e até uma pitada de humor. O bot responde automaticamente a mensagens e menciona tópicos comuns entre torcedores, como títulos, comparações entre times e ídolos do Palmeiras, com o objetivo de simular o tom e a energia de um torcedor típico em redes sociais. Esse projeto é ideal para divertir e interagir com outros torcedores e amantes de futebol, proporcionando respostas autênticas e personalizadas.

## 🤖 Tecnologias Utilizadas
- **OpenAI GPT-3.5**: para geração de respostas em linguagem natural, simulando o estilo de um torcedor fanático.
- **Python**: linguagem para desenvolvimento do bot.
- **Python Telegram Bot API**: para integração com o Telegram e gerenciamento de mensagens.

## 🧐 Processo de Criação
1. **Preparação do Estilo de Resposta**: Após observar o tom e o tipo de linguagem usados por torcedores palmeirenses nas redes, foram criados prompts para o GPT-3.5, focados em imitar a paixão e humor característicos.
2. **Configuração do Bot no Telegram**: Foi criado um bot pelo BotFather do Telegram para gerar o token e configurar permissões de uso.
3. **Integração com a API GPT-3.5**: Utilizei a API da OpenAI para fazer com que o bot gere respostas automáticas baseadas nas mensagens que o usuário mandar.

## 📝 Como Usar

1. **Instalação**:
   - Clone o repositório para seu ambiente local:
     ```bash
     git clone https://github.com/fornari03/lab-natty-or-not.git
     ```
   - Crie um ambiente virtual e instale as dependências necessárias:
     ```bash
     pip install -r requirements.txt
     ```
   - Crie um arquivo `.env` com as variáveis 
     ```py
     OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
     TELEGRAM_BOT_TOKEN="YOUR_TELEGRAM_BOT_TOKEN"
     ```
    - Crie uma conta na OpenAI que tenha crédito e crie uma API Key, alterando o valor da respectiva variável no arquivo `.env`.

    - Abra o app do Telegram e comece uma conversa com o [BotFather](https://core.telegram.org/bots#botfather), mandando as seguintes mensagens em ordem:
        ```
        /start

        /newbot

        torcedor-palmeiras

        torcedor_palmeiras_bot
        ```
    - Copie o token dado pelo BotFather e altere o valor da respectiva variável no arquivo `.env`.

2. **Execução**:
   - Execute o bot com o comando:
     ```bash
     python main.py
     ```
   - Agora, o bot está ativo e pronto para responder a mensagens no Telegram!

3. **Interação no Telegram**:
   - No aplicativo do Telegram, busque por `torcedor-palmeiras` e inicie uma conversa.
   - Mande mensagens relacionadas ao Palmeiras ou futebol, como "Quem é o maior time do Brasil?" ou "Quantos títulos o Palmeiras tem?" e o bot responderá como um verdadeiro torcedor fanático!
   - Para grupos de torcedores, adicione o bot ao grupo e permita que ele responda automaticamente aos membros.

> **Nota**: Para um uso mais avançado, configure o bot para filtrar mensagens específicas, responder com imagens de memes e até comparar jogadores, tudo a partir de prompts personalizados com a API OpenAI. No entanto, tudo deve gerar mais custos na sua conta da OpenAI, então tenha cautela.



## 🚀 Resultados
O bot foi capaz de:
- Responder de forma convincente a perguntas sobre o Palmeiras, como conquistas, jogadores lendários, e rivalidades, utilizando uma linguagem que reflete o espírito de um verdadeiro torcedor.
- Engajar usuários do Telegram que interagem com ele, respondendo de maneira rápida e com um toque de humor.
- Reagir a menções e tópicos específicos com assertividade, fazendo uso das capacidades de linguagem natural do GPT-3.5 para gerar respostas que parecem espontâneas e naturais, apesar de não parecer 100% um ser humano respondendo.

## 💭 Reflexão
Criar o "Torcedor Palmeiras Bot" foi um exercício divertido e desafiador, exigindo uma especificação maior dos prompts para que o tom ficasse o mais próximo possível do que se espera de um torcedor fanático. Um dos principais desafios foi evitar que o bot se tornasse repetitivo e ao mesmo tempo garantir que suas respostas mantivessem a personalidade. A experiência mostra como a IA pode gerar interações interessantes quando bem calibrada com contexto específico, dando vida a um "torcedor virtual" autêntico e entusiasmado.

Um ponto negativo é que para testar o projeto, deve-se ter uma conta com crédito na OpenAI, caso contrário o bot não funciona, retornando apenas a mensagem inicial de saudações.
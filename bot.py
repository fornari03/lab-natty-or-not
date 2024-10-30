from telegram import Update
from telegram.ext import ContextTypes
import openai

class PalmeirasBot:
    async def get_palmeiras_response(self, user_message):
        conversation = [
            {"role": "system", "content": "Você é um torcedor apaixonado pelo Palmeiras, defendendo que o Palmeiras é o maior time do Brasil. Você responde de forma casual e informal, como se estivesse no twitter ou no reddit. Evite emojis e escreva com letras minúsculas. Pode falar sobre qualquer assunto relacionado ao Palmeiras, como jogadores, títulos, rivalidades, etc, além de poder insultar/zoar o time do usuário caso não seja o palmeiras. Caso pergunte sobre algo que não seja relacionado ao Palmeiras ou futebol, diga que só sabe falar sobre o Palmeiras. Exemplo de uma frase que você poderia dizer: 'o palmeiras é o maior time do brasil, irmão, sem mais.' ou 'eai mano, vc é verdão ou é anti?'"},
            {"role": "user", "content": user_message}
        ]
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0125",
            temperature=0.8,
            max_tokens=3000,
            messages=conversation
        )
        
        assistant_reply = response['choices'][0]['message']['content']
        return assistant_reply


    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_message = update.message.text
        response = await self.get_palmeiras_response(user_message)
        await update.message.reply_text(response)

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text('eai mano, vc é verdão ou é anti?')
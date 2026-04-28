import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

async def calculate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    try:
        allowed = set("0123456789+-*/(). ")
        if not all(c in allowed for c in text):
            await update.message.reply_text("❌ ဂဏန်းနှင့် +-*/ သာ သုံးပါ")
            return
        result = eval(text)
        reply = f"{text} = {result:,}"
        await update.message.reply_text(reply)
    except:
        await update.message.reply_text("❌ မှားနေတယ်၊ ထပ်ကြိုး")

TOKEN = os.environ.get("TOKEN")
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, calculate))
app.run_polling()

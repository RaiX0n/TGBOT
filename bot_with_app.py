import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

TELEGRAM_BOT_TOKEN = "8282174338:AAFItIgBvd1ZY4uCjnJRP38TnaJsavx-wKg"

class MiniAppBot:
    def __init__(self):
        self.application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
        self.setup_handlers()
    
    def setup_handlers(self):
        """Регистрируем все обработчики команд"""
        self.application.add_handler(CommandHandler("start", self.start))
        self.application.add_handler(CommandHandler("app", self.open_app))
        self.application.add_handler(CommandHandler("help", self.help))
        self.application.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, self.handle_web_app_data))
    
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Обработчик команды /start"""
        user = update.effective_user
        
        #Кнопки для Mini App
        keyboard = [
            [InlineKeyboardButton(
                "🚀 Открыть Mini App", 
                web_app=WebAppInfo(url="https://raix0n.github.io/TGBOT/")
            )]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_text(
            f"👋 Привет, {user.first_name}!\n\n"
            "Я бот с Mini App - это веб-приложение прямо в Telegram! 📱\n\n"
            "Нажми кнопку ниже чтобы открыть:",
            reply_markup=reply_markup
        )
    
    async def open_app(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Команда /app для быстрого доступа к приложению"""
        keyboard = [
            [InlineKeyboardButton(
                "📱 Открыть приложение", 
                web_app=WebAppInfo(url="https://raix0n.github.io/TGBOT/")
            )]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("Открываю Mini App...", reply_markup=reply_markup)
    
    async def help(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Команда /help"""
        help_text = """
🤖 ДОСТУПНЫЕ КОМАНДЫ:

/start - Начать работу с ботом
/app - Открыть Mini App
/help - Показать эту справку

🎯 Mini App - это веб-приложение которое работает прямо в Telegram!
        """
        await update.message.reply_text(help_text)
    
    async def handle_web_app_data(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Обрабатываем данные, отправленные из Mini App"""
        web_app_data = update.message.web_app_data
        data = web_app_data.data  # Данные которые мы отправили из приложения
        
        await update.message.reply_text(
            f"📨 Получены данные из Mini App:\n"
            f"`{data}`\n\n"
            f"✅ Отлично! Mini App работает и может общаться с ботом!",
            parse_mode='Markdown'
        )
    
    def run(self):
        """Запуск бота"""
        print("🤖 Бот с Mini App запускается...")
        print("⭐ Твой Mini App доступен по адресу: https://raix0n.github.io/TGBOT/")
        self.application.run_polling()

if __name__ == "__main__":
    bot = MiniAppBot()
    bot.run()
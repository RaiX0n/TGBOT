import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

TELEGRAM_BOT_TOKEN = "8282174338:AAFItIgBvd1ZY4uCjnJRP38TnaJsavx-wKg"

class AdvancedBot:
    def __init__(self):
        self.application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
        self.setup_handlers()
    
    def setup_handlers(self):
        """Регистрируем все обработчики"""
        # Основные команды
        self.application.add_handler(CommandHandler("start", self.start))
        self.application.add_handler(CommandHandler("help", self.help))
        self.application.add_handler(CommandHandler("profile", self.profile))
        self.application.add_handler(CommandHandler("balance", self.balance))
        self.application.add_handler(CommandHandler("settings", self.settings))
        
        # Mini App
        self.application.add_handler(CommandHandler("app", self.open_app))
        self.application.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, self.handle_web_app_data))
    
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Команда /start с кнопками"""
        user = update.effective_user
        
        keyboard = [
            [InlineKeyboardButton("🚀 Открыть приложение", web_app=WebAppInfo(url="https://raix0n.github.io/TGBOT/"))],
            [InlineKeyboardButton("👤 Профиль", callback_data="profile"),
             InlineKeyboardButton("💰 Баланс", callback_data="balance")],
            [InlineKeyboardButton("⚙️ Настройки", callback_data="settings"),
             InlineKeyboardButton("ℹ️ Помощь", callback_data="help")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_text(
            f"👋 Привет, {user.first_name}!\n\n"
            "Я многофункциональный бот! Выбери действие ниже или используй команды:\n"
            "• /profile - твой профиль\n"
            "• /balance - баланс\n" 
            "• /settings - настройки\n"
            "• /app - открыть приложение\n"
            "• /help - все команды",
            reply_markup=reply_markup
        )
    
    async def help(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Команда /help - показывает все команды"""
        help_text = """
📋 **ДОСТУПНЫЕ КОМАНДЫ:**

👤 **Профиль:**
/profile - Информация о профиле
/balance - Баланс и статистика

⚙️ **Настройки:**
/settings - Настройки бота
/notifications - Управление уведомлениями

📱 **Приложение:**
/app - Открыть Mini App
/web - Веб-версия

ℹ️ **Помощь:**
/help - Эта справка
/support - Техподдержка

💡 **Совет:** Все функции также доступны в Mini App!
        """
        await update.message.reply_text(help_text, parse_mode='Markdown')
    
    async def profile(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Команда /profile - информация о пользователе"""
        user = update.effective_user
        
        profile_text = f"""
👤 **Твой профиль:**

**Имя:** {user.first_name}
**ID:** {user.id}
**Username:** @{user.username or 'не указан'}

📊 **Статистика:**
• Зарегистрирован: Сегодня
• Команд использовано: 5
• Активность: Высокая

💡 Используй /balance для финансов или открой приложение для полного функционала!
        """
        await update.message.reply_text(profile_text, parse_mode='Markdown')
    
    async def balance(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Команда /balance - показывает баланс"""
        balance_text = """
💰 **Твой баланс:**

**Основной счет:** 1 000 ₽
**Бонусы:** 150 ₽
**Кешбэк:** 45 ₽

📈 **За сегодня:**
• Пополнений: +500 ₽
• Расходов: -350 ₽

💡 Подробная статистика в приложении! Нажми /app
        """
        await update.message.reply_text(balance_text, parse_mode='Markdown')
    
    async def settings(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Команда /settings - настройки"""
        settings_text = """
⚙️ **Настройки бота:**

🔔 **Уведомления:** Включены
🌐 **Язык:** Русский
🎨 **Тема:** Авто

🔒 **Безопасность:**
• 2FA: Выключено
• СМС-подтверждение: Включено

💡 Для детальных настроек открой приложение: /app
        """
        
        keyboard = [
            [InlineKeyboardButton("🔔 Уведомления", callback_data="notifications"),
             InlineKeyboardButton("🌐 Язык", callback_data="language")],
            [InlineKeyboardButton("🎨 Тема", callback_data="theme"),
             InlineKeyboardButton("📱 Приложение", web_app=WebAppInfo(url="https://raix0n.github.io/TGBOT/"))]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_text(settings_text, reply_markup=reply_markup, parse_mode='Markdown')
    
    async def open_app(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Команда /app - открывает Mini App"""
        keyboard = [[InlineKeyboardButton("📱 Открыть приложение", web_app=WebAppInfo(url="https://raix0n.github.io/TGBOT/"))]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("Открываю полнофункциональное приложение...", reply_markup=reply_markup)
    
    async def handle_web_app_data(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Обрабатывает данные из Mini App"""
        web_app_data = update.message.web_app_data
        data = web_app_data.data
        
        # Обрабатываем разные типы данных из Mini App
        if data.startswith("profile:"):
            await update.message.reply_text("📊 Данные профиля получены из приложения!")
        elif data.startswith("balance:"):
            await update.message.reply_text("💰 Финансовая информация обновлена!")
        elif data.startswith("settings:"):
            await update.message.reply_text("⚙️ Настройки сохранены!")
        else:
            await update.message.reply_text(f"📨 Получено из приложения: {data}")

    def run(self):
        print("🤖 Продвинутый бот запущен...")
        print("💡 Теперь есть команды и подсказки!")
        self.application.run_polling()

if __name__ == "__main__":
    bot = AdvancedBot()
    bot.run()

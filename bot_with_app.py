<!DOCTYPE html>
<html>
<head>
    <title>Многофункциональное приложение</title>
    <script src="https://telegram.org/js/telegram-web-app.js"></script>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: var(--bg-color, #667eea);
            color: var(--text-color, #ffffff);
            margin: 0;
            padding: 0;
            transition: all 0.3s;
        }
        
        .container {
            max-width: 400px;
            margin: 0 auto;
            padding: 20px;
        }
        
        .header {
            text-align: center;
            margin-bottom: 30px;
            padding: 20px 0;
        }
        
        .app-title {
            font-size: 24px;
            font-weight: bold;
            margin: 0;
        }
        
        .app-subtitle {
            opacity: 0.8;
            margin: 5px 0 0 0;
        }
        
        .card {
            background: var(--card-bg, rgba(255,255,255,0.1));
            border-radius: 15px;
            padding: 20px;
            margin-bottom: 20px;
            backdrop-filter: blur(10px);
        }
        
        .btn {
            background: var(--btn-bg, #764ba2);
            color: white;
            border: none;
            border-radius: 10px;
            padding: 15px;
            margin: 5px 0;
            cursor: pointer;
            font-size: 16px;
            width: 100%;
            transition: background 0.3s;
        }
        
        .btn:hover {
            background: var(--btn-hover, #5a3890);
        }
        
        .commands-list {
            background: rgba(0,0,0,0.2);
            border-radius: 10px;
            padding: 15px;
            margin: 10px 0;
        }
        
        .command-item {
            padding: 8px 0;
            border-bottom: 1px solid rgba(255,255,255,0.1);
        }
        
        .command-item:last-child {
            border-bottom: none;
        }
        
        .command-name {
            font-weight: bold;
        }
        
        .command-desc {
            opacity: 0.8;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- ЗАГОЛОВОК -->
        <div class="header">
            <h1 class="app-title">🚀 Мое приложение</h1>
            <p class="app-subtitle">Все функции в одном месте!</p>
        </div>
        
        <!-- БЫСТРЫЕ ДЕЙСТВИЯ -->
        <div class="card">
            <h3>⚡ Быстрые действия</h3>
            <button class="btn" onclick="openProfile()">👤 Мой профиль</button>
            <button class="btn" onclick="openBalance()">💰 Баланс</button>
            <button class="btn" onclick="openSettings()">⚙️ Настройки</button>
            <button class="btn" onclick="sendToBot('help')">ℹ️ Помощь</button>
        </div>
        
        <!-- КОМАНДЫ ДЛЯ ЧАТА -->
        <div class="card">
            <h3>💬 Команды для чата</h3>
            <div class="commands-list">
                <div class="command-item">
                    <div class="command-name">/start</div>
                    <div class="command-desc">Начать работу с ботом</div>
                </div>
                <div class="command-item">
                    <div class="command-name">/profile</div>
                    <div class="command-desc">Информация о профиле</div>
                </div>
                <div class="command-item">
                    <div class="command-name">/balance</div>
                    <div class="command-desc">Баланс и статистика</div>
                </div>
                <div class="command-item">
                    <div class="command-name">/settings</div>
                    <div class="command-desc">Настройки бота</div>
                </div>
                <div class="command-item">
                    <div class="command-name">/help</div>
                    <div class="command-desc">Все доступные команды</div>
                </div>
                <div class="command-item">
                    <div class="command-name">/app</div>
                    <div class="command-desc">Открыть это приложение</div>
                </div>
            </div>
        </div>
        
        <!-- ИНФОРМАЦИЯ О ПОЛЬЗОВАТЕЛЕ -->
        <div class="card">
            <h3>📊 Мои данные</h3>
            <div id="userData">Загрузка...</div>
        </div>
    </div>

    <script>
        // TELEGRAM WEB APP API
        const tg = window.Telegram.WebApp;
        
        // ИНИЦИАЛИЗАЦИЯ
        tg.expand();
        tg.ready();
        
        // ЗАГРУЗКА ДАННЫХ ПОЛЬЗОВАТЕЛЯ
        function loadUserData() {
            const user = tg.initDataUnsafe.user;
            if (user) {
                document.getElementById('userData').innerHTML = `
                    <p><strong>Имя:</strong> ${user.first_name}</p>
                    <p><strong>ID:</strong> ${user.id}</p>
                    <p><strong>Username:</strong> @${user.username || 'не указан'}</p>
                    <p><strong>Язык:</strong> ${tg.initDataUnsafe.user.language_code || 'не указан'}</p>
                `;
            }
        }
        
        // ФУНКЦИИ ПРИЛОЖЕНИЯ
        function openProfile() {
            tg.sendData("profile:open");
            alert('📊 Открываю профиль...');
        }
        
        function openBalance() {
            tg.sendData("balance:open");
            alert('💰 Открываю баланс...');
        }
        
        function openSettings() {
            tg.sendData("settings:open");
            alert('⚙️ Открываю настройки...');
        }
        
        function sendToBot(action) {
            tg.sendData(action);
            // tg.close(); // Можно закрыть после отправки
        }
        
        // АВТОМАТИЧЕСКАЯ ЗАГРУЗКА ДАННЫХ
        loadUserData();
    </script>
</body>
</html>

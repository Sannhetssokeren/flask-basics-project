from flask import Flask

# Создаем экземпляр Flask-приложения
app = Flask(__name__)

# Определяем маршрут для главной страницы '/'
@app.route('/')
def hello_world():
    return '<h1>Hello, Flask!</h1><p>Это мое первое Flask-приложение.</p>'

# Проверяем, что скрипт запущен напрямую, а не импортирован
if __name__ == '__main__':
    # Запускаем веб-сервер в режиме отладки
    # ВНИМАНИЕ: debug=True использовать ТОЛЬКО при разработке!
    app.run(debug=True)
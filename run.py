from app import create_app

# Создаем приложение
app = create_app()

if __name__ == "__main__":
    # Запускаем приложение на порту 10000, так как Render требует его
    app.run(host="0.0.0.0", port=10000)

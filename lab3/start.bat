# Создадим и обучи модель
python src/create_model.py

# Запустим API сервис
# Если вам нужно только локальное подключение, используйте 127.0.0.1.
# Если вы хотите, чтобы другие устройства в вашей сети могли обращаться к вашему серверу, используйте 0.0.0.0.
uvicorn src.api_app:app --host 0.0.0.0 --port 8000
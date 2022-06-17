# Тестовое задание для Физтех.Центра

## Описание
Телеграм бот, позволяющий проверять, валиден ли ИНН юридического или физического лица.


## Установка локально
1. Склонировать репозиторий
```
git clone git@github.com:shamaevnn/phystech_centre_test_bot.git && cd phystech_centre_test_bot
```
2. Создать виртуальное окружение
```
python3 -m venv venv
source venv/bin/activate
```
3. Установить зависимости
```
pip install -r requirements.txt
```
4. Создать `.env` файл, прописав там свой `TELEGRAM_TOKEN`
```
cp .env_example .env
```

## Запуск бота в polling mode
```
python3 run_polling.py
```

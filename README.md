# Тестовое задание для Физтех.Центра

## Описание
Телеграм бот, позволяющий проверять, валиден ли ИНН юридического или физического лица.
Проверка осуществляется по [этому алгоритму](https://ru.wikipedia.org/wiki/%D0%98%D0%B4%D0%B5%D0%BD%D1%82%D0%B8%D1%84%D0%B8%D0%BA%D0%B0%D1%86%D0%B8%D0%BE%D0%BD%D0%BD%D1%8B%D0%B9_%D0%BD%D0%BE%D0%BC%D0%B5%D1%80_%D0%BD%D0%B0%D0%BB%D0%BE%D0%B3%D0%BE%D0%BF%D0%BB%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D1%89%D0%B8%D0%BA%D0%B0#%D0%92%D1%8B%D1%87%D0%B8%D1%81%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5_%D0%BA%D0%BE%D0%BD%D1%82%D1%80%D0%BE%D0%BB%D1%8C%D0%BD%D1%8B%D1%85_%D1%86%D0%B8%D1%84%D1%80)

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

# Sprint 6 — UI tests for Yandex Scooter

## Описание проекта

Автоматизированные UI-тесты сервиса Яндекс Самокат.

Проект реализован с использованием паттерна Page Object.

## Используемые технологии

- Python 3.11
- Selenium
- Pytest
- Allure
- Firefox WebDriver

## Структура проекта

pages/
tests/
data.py
urls.py
conftest.py

## Запуск тестов

```bash
pytest -v
```

## Генерация Allure-отчёта

```bash
pytest --alluredir=allure-results
allure serve allure-results
```
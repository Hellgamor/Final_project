# Описание проекта:
Тестирование учебного приложения Яндекс Самокат. Яндекс Самокат - это сервис, который позволяет арендовать электрический самокат на несколько дней.
Проект состоит из двух частей: 
1. Регрессионное тестирование и ретест багов в приложении.
2. Работа с базой данных и автоматизация.

- Язык приложения — `JavaScript`.
- Среда - `Node.js v12.17.0`
- Доступ к приложению по протоколу `HTTP 1.1`.
- Документация к приложению осуществляется с помощью модуля `apiDoc`.
- Приложение использует базу данных — `PostgreSQL`.

## 1. Регрессионное тестирование и ретест багов в приложении

### Задание 1 
Необходимо провести тестирование функциональности "Сделать заказ" в Яндекс Самокате, в том числе и кроссбраузерное.
Чек-лист с результатами проверок находится по ссылке: https://docs.google.com/spreadsheets/d/1iuz7Yh5LdFsx6Q8emo7kL6MSHJi7GWXDS8LQy7yTulY/edit?usp=sharing

### Задание 2
Необходимо провести регрессионное тестирование по готовым тест-кейсам.
Результаты тестирования расположены по ссылке: https://docs.google.com/spreadsheets/d/1z3P2ePPts6_VB6s9feiv8ghnnXBomIUC9RkHAHxO0UQ/edit?usp=sharing


## 2. Работа с базой данных
Во второй части представлена работа с базой данных и автоматизация 
теста Яндекс Самоката. 
Запросы расположены в файле `SQL.md`, результаты выполнения запросов расположены 
в файлах `sql_query_1.png` и `sql_query_2.png`

### Задание 1
Нужно проверить, отображается ли созданный заказ в базе данных.
Для этого необходимо вывести список логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true). 

### Задание 2

Надо протестировать статусы заказов. Нужно убедиться, что в базе данных они записываются корректно.
Для этого необходимо вывести все трекеры заказов и их статусы. 
Статусы определяются по следующему правилу:
Если поле finished == true, то вывести статус 2.
Если поле canсelled == true, то вывести статус -1.
Если поле inDelivery == true, то вывести статус 1.
Для остальных случаев вывести 0.

## 2. Автоматизация теста.
Автотест расположен в файле `sender_stand_request.py`, результаты выполнения автотеста расположены 
в файле `autotest_results.png`
### Задание
Необходимо автоматизировать сценарий, который подготовили тестировщики:
1. Клиент создает заказ.  
2. Проверяется, что по треку заказа можно получить данные о заказе.

### Требования

- Для запуска тестов должны быть установлены пакеты `pytest` и `requests`.
- Запуск всех тестов выполняется командой `pytest`.

### Шаги выполнения автотеста

1. Для запуска теста необходимо в файл configuration.py вставить актуальный URL стенда (пример: 
https://68b0eca5-2eab-424b-aa7a-b56d7c658e73.serverhub.praktikum-services.ru)
2. В файле sender_stand_request.py нажать кнопку Run или ввести в терминале команду `pytest`

## Стек для выполнения проекта
* PyCharm
* GitHub
* requests
* pytest

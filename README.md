
# Реализованная функциональность  
- Анализ текста и поиск ключевых слов с использованием библиотеки машинного обучения SciKitLearn 
- Поиск информации в Google, Youtube, Google Images по заданной тематике
- Возможность оценивать сайты (система рейтинга)
- Возможность блокировки сайтов

# Особенность проекта в следующем:
Любой пользователь может получить подборку релевантной информации, которая агрегируется из самых популярных источников  

# Основной стек технологий:
- Фронтенд - VueJS
- Бэкенд - Flask
- БД - MongoDB

# Демо
### Приложение доступно по адресу: https://obuchalochka.flint3s.ru
### Скринкаст доступен по адресу: https://disk.yandex.ru/d/Kkh89gBWBCeoyA

# НЕОБХОДИМЫЕ УСЛОВИЯ ДЛЯ РАБОТЫ ПРИЛОЖЕНИЯ
1. Развертывание сервиса производится на ubuntu linux
2. Требуется установленный web-сервер (рек. nginx);
3. Требуется NoSQL БД MongoBD (возможно использование облачной БД);

# Развертывание
## Бэкенд
Бэкенд - классическое Flask-приложение, для его развертывания нужен WSGI-сервер (например, gunicorn)  

Запуск производится следующим образом: gunicorn main:app [--parameters]  

При необходимости можно использовать таск-менеджеры (systemd, pm2 и другие)  

HTTP-сервер при этом должен быть настроен на проксирование порта, где находится приложение (по умолчанию 5000)  

Все необходимые зависимости указаны в файле requirements.txt (установка через pip install -r requirements.txt)


## Фронтенд  
Фронтенд представляет из себя Vue-веб-приложение  

Для начала работы следует установить все зависимости командой ```npm i``` в папке проекта  

Для режима разработки используется hot-reload сервер, запускающийся командой ```npm run serve```

Для создания билда проекта используется команда ```npm run build```

Адрес бэкенда приложения указывается в файле ```backend.config.js```

После выполнения ```npm run build``` появляется папка ```dist```, в которой находятся все статические файлы приложения. Для его функционирования следует просто настроить Nginx (или другой сервер) на отдачу статики



# РАЗРАБОТЧИКИ  
### И наши юзернеймы в Telegram  

Самойлов Илья - Fullstack @siailya
Захаров Филип - Backend @Pholeg
Козлов Тимофей - Backend @zerodaayy
Шиняева Анастасия - Design @adoomaxas
Чернов Тимофей - Analytics @tubeornot

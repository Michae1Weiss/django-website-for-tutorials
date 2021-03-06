[**English**](README.md) | **Russian**
# Django вебсайт для уроков
Сайт для публикации уроков с аккуратным дизайном и отзывчивым интерфейсом.

## Особенности
* Django
  * Веб фреймворк
  * [GitHub репозиторий](https://github.com/django/django)
* Python-Markdown
  * Конвертация строки в HTML
  * [GitHub репозиторий](https://github.com/Python-Markdown/markdown/)
* python-dotenv
  * Считывает пары ключ-значение из файла .env и может устанавливать их в качестве переменных окружения
  * [GitHub репозиторий](https://github.com/theskumar/python-dotenv)
* mini.css
  * Минималистичный, отзывчивый и неприхотливый CSS фреймворк
  * [GitHub репозиторий](https://github.com/Chalarangelo/mini.css/)

## Как запустить (Linux, MacOS)
1. **Перейди** в папку с проектами и **клонируй** репозиторий локально
    ```bash
    # перейди в папку, куда ты хочешь клонировать репозиторий
    $ cd /path/to/project/folder/
    # клонируй этот несчастный репозиторий
    $ git clone https://github.com/Michae1Weiss/django-website-for-tutorials.git
    ```
2. Зайди в папку репозитория
    ```bash
    # перейди в папку
    $ cd django-website-for-tutorials
    ```
3. Создай **виртуальное окружение** для Python и **активируй** его.
[Доступно о виртуальном окружении (на русском)](https://ru.hexlet.io/courses/python-setup-environment/lessons/venv/theory_unit)
    > В системе должен быть установлен **Python** версии 3.6+. [Скачать питон](https://www.python.org/downloads/)
    ```bash
    # создай виртуальное окружение
    $ python3 -m venv venv 
    # [!] python создаст папку `venv`
    # активируй виртуальное окружение
    $ source venv/bin/activate
    ```
    > В командной строке перед именем должна появится надпись `(venv)`. Для выхода из окружения напиши `deactivate`.
4. Проведи миграцию базы данных [О команде **migrate**](https://docs.djangoproject.com/en/4.0/ref/django-admin/#migrate)
   ```bash
   # это создаст файл базы данных `db.sqlite3` со всеми необходимыми таблицами
   $ python manage migrate
   ```
5. Собери статические файлы. [О команде **collectstatic**](https://docs.djangoproject.com/en/4.0/ref/django-admin/#collectstatic)
   ```bash
   # Это стянет все необходимые статические файлы в одну общую папку `static` в корне проекта.
   $ python manage collectstatic
   ```
6. Запусти сервер. [О команде **runserver**](https://docs.djangoproject.com/en/4.0/ref/django-admin/#runserver)
   ```bash
   # По умолчанию запускает сервер локально: http://127.0.0.1:8000
   $ python manage runserver
   ```
7. Создай суперпользователя. [О команде **createsuperuser**](https://docs.djangoproject.com/en/4.0/ref/django-admin/#createsuperuser)
   ```bash
   # Нужно для того чтобы иметь возможность создавать уроки в админ панели.
   $ python manage createsuperuser
   ```
8. **Поздравляю**, теперь ты можешь пользоваться сайтом :)

## Советы начинающим программистам
> Практика - путь к совершенству. ~ пословица
1. Ты **не сможешь научиться** программировать **только читая** об этом. Единственный способ научиться - это **реально кодить**. 
2. Не беспокойся о том, что ты учишь не то, что нужно. **Любой язык**, который ты выберешь, поможет тебе изучить основные концепции программирования.
3. Как только ты освоишь **один** язык, второй будет изучать гораздо легче. Поэтому не позволяй ["параличу решений"](https://mind-practice.com/paralichanaliza) помешать тебе начать.
4. Использование **Google** для поиска ответа - это **не читерство**. Также как и просмотр кода, который ты написал в прошлом. 
5. **Ошибаться** - это **нормально**, и ты должен быть уверен, что ошибки - это нормально.
6. Есть 4 вещи, которые ты можешь сделать, чтобы убедиться, что ты просишь о помощи правильно:
   1. Пересказывай детали, которые ты видишь. Не стесняйся включать дополнительные детали, которые могут быть кому-то интересны, но могут и не понадобиться. 
   2. Объясни, что именно, по твоему мнению, должно происходить. 
   3. Объясни, что происходит на самом деле. 
   4. Объясни, почему ты считаешь, что все должно работать по-другому.
7. Не думай, что ты должен быть математическим гением, чтобы хорошо программировать.
8. Если ты только начинаешь учиться, ты должен быть готовым переписывать свой код, чтобы довести его до лучшего состояния.
   * Мы называем это [рефакторингом](https://ru.wikipedia.org/wiki/%D0%A0%D0%B5%D1%84%D0%B0%D0%BA%D1%82%D0%BE%D1%80%D0%B8%D0%BD%D0%B3)
9. В программировании **можно** принимать факты по мере их усвоения. 
   * Не нужно лезть в каждую [кроличью нору](https://ru.wikipedia.org/wiki/%D0%9A%D1%80%D0%BE%D0%BB%D0%B8%D1%87%D1%8C%D1%8F_%D0%BD%D0%BE%D1%80%D0%B0_%D0%B2%D0%B8%D0%BA%D0%B8) в поисках ответа на вопрос _"а почему так?"_.
10. Иногда тебе может казаться, что ты понятия не имеешь, что делаешь. И это **нормально**.
11. Изучение кода - это большой труд. Поэтому самое худшее, что ты можешь сделать, - это сдаться прямо перед тем, как ты увидишь результаты. 

## Sources:
* [Вещи, которые никогда не следует делать во время изучения кода (на английском)](http://blog.thefirehoseproject.com/posts/the-14-things-you-should-never-do-while-learning-to-code/)
* [Шпаргалка для работы с git (на английском)](https://training.github.com/downloads/ru/github-git-cheat-sheet/)
* [Гайд по работе с git + гайд по Python (на русском)](https://pyneng.readthedocs.io/ru/latest/book/02_git_github/git_basics.html)
* [Бесплатные интерактивные уроки по Python](https://ru.code-basics.com/languages/python)
* [Книга украинца о Python, WEB и Django](https://github.com/AndreyBulezyuk/Django-3-Book)
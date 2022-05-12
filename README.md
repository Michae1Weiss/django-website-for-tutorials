**English** | [**Russian**](README_RU.md)
# Django website for tutorials
A site for publishing tutorials with a clean design and responsive interface.

## Features
* Django
  * Web framework
  * [GitHub repo](https://github.com/django/django)
* Python-Markdown
  * Converts string to HTML
  * [GitHub repo](https://github.com/Python-Markdown/markdown/)
* python-dotenv
  * Reads key-value pairs from a .env file and can set them as environment variables
  * [GitHub repo](https://github.com/theskumar/python-dotenv)
* mini.css
  * Minimal, responsive, style-agnostic CSS framework
  * [GitHub repo](https://github.com/Chalarangelo/mini.css/)

## How to (Linux, MacOS)

1. **Go** to your project folder and **clone** the repository locally
    ```bash
    # go to the folder where you want to clone the repository
    $ cd /path/to/project/folder/
    # clone this repository
    $ git clone https://github.com/Michae1Weiss/django-website-for-tutorials.git
    ```
2. Go into the repository folder
    ```bash
    # go to the folder
    $ cd django-website-for-tutorials
    ```
3. Create a **virtual environment** for Python and **activate** it.
[About virtual environment (in English)](https://www.dabapps.com/blog/introduction-to-pip-and-virtualenv-python/)
    > **Python** version 3.6+ must be installed on your system. [Download python](https://www.python.org/downloads/)
    ```bash
    # create a virtual environment
    $ python3 -m venv venv 
    # [!] python will create a `venv` folder
    # activate the virtual environment
    $ source venv/bin/activate
    ```
    > On the command line you should see `(venv)` in front of the name. To exit the environment write `deactivate`.
4. Do a database migration [About **migrate** command](https://docs.djangoproject.com/en/4.0/ref/django-admin/#migrate)
   ```bash
   # This will create a database file `db.sqlite3` with all the necessary tables
   $ python manage migrate
   ```
5. Collect static files. [About **collectstatic** command](https://docs.djangoproject.com/en/4.0/ref/django-admin/#collectstatic)
   ```bash
   # This will pull all the necessary static files into one common `static` folder in the root of the project.
   $ python manage collectstatic
   ```
6. Run the server. [About **runserver** command](https://docs.djangoproject.com/en/4.0/ref/django-admin/#runserver)
   ```bash
   # By default launches the server locally: http://127.0.0.1:8000
   $ python manage runserver
   ```
7. Create a superuser. [About **createsuperuser** command](https://docs.djangoproject.com/en/4.0/ref/django-admin/#createsuperuser)
   ```bash
   # You need it to be able to create lessons in the admin panel.
   $ python manage createsuperuser
   ```
8. **Congratulations**, now you can use this website :)

## Tips for beginner programmers
> Practice makes perfect. ~ Traditional Proverb
1. You can’t learn to code by reading about it. The only way to learn is by actually coding. 
2. Don’t worry about learning the wrong thing. Any language that you pick will at least help you learn the concepts central to programming.
3. Once you master one language, picking up a second language is much easier. So don’t let an analysis paralysis prevent you from ever starting.
4. Using Google to find an answer isn’t cheating. Neither is looking at code that you’ve written in the past. 
5. Screwing up is normal, and you need to have the attitude that it’s ok to make mistakes.
6. There are 4 things that you can do to make sure that you’re asking for help in the right way:
   1. Overcommunicate details that you see.  Feel free to include additional details someone might want to know, but also might not be needed. 
   2. Explain exactly what you think should be happening. 
   3. Explain exactly what is actually happening. 
   4. Explain why you think it should be working differently.
7. Don't think you have to be a mathematical genius to be good at programming.
8. If you’re just starting to learn, you need to be open to changing your code to get it to a better state.
9. In programming, it’s ok to accept the facts as you learn them. 
   * You don’t need to go down every rabbit hole in search of the answer to _“how come it’s like that?”_
10. You might feel like you have no idea what you’re doing sometimes. And that’s ok.
11. Learning to code is a lot of work. So the worst thing you can do is give up right before you’re about to see results. 

## Sources:
[Things you should never do while learning to code](http://blog.thefirehoseproject.com/posts/the-14-things-you-should-never-do-while-learning-to-code/)

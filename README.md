Steps for deployment

1. create virtual environment:
$ python3 -m venv env
$ source env/bin/activate

2. Install flask, gunicorn, and other dependencies for app

3. $ heroku login

4. $ git init

5. add "web: gunicorn app:app" to Procfile

6. add "env" to .gitignore

7. pip freeze > requirements.txt

8. git add .

9. git commit -m ""

10. git push heroku master

11. heroku ps:scale web=1

12. heroku open 
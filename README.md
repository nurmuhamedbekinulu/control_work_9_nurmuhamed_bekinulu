Склонировать файлы приложения в локальную папку для этого откройте командную строку в выбранной папке с помощью команды в  gh repo clone nurmuhamedbekinulu/control_work_9_nurmuhamed_bekinulu
создайте виртулальное окружение командой python3 -m venv venv
установите зависимости, скачав все нужные библиотеки python3 -m pip install -r requirements.txt  (или pip install -r requirements.txt  ) данную команду выполните в папке где находится файл requirements.txt.
необходимо установить бд подбробное описание можете прочитать в статье https://www.digitalocean.com/community/tutorials/how-to-install-postgresql-on-ubuntu-20-04-quickstart-ru
в папке "app" найдите фалй settings.py   "NAME": "имя_вашей_бд", "USER": "имя_пользователя_бд",  "PASSWORD": "пароль",
в папке где находится файл manage.py запустите командную строку введите python3 manage.py runserver и можете использовать приложение открыв следующую ссылку в браузере  http://localhost:8000/

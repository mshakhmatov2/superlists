Обеспечение работы нового сайта
===========================

Необходимые пакеты 
* nginx
* Python
* virtualenv + pip
* Git например, в Ubuntu:

    sudo add-apt-repository ppa:fkrull/deadsnakes

    sudo apt-get install nginx git python36 python3.6-venv 

## Конфигурация виртуального узла Nginx
*	см. nginx.template.conf
*	заменить SITENAME, например, на staging.my-domain.com

## Служба Systemd
*	см. gunicorn-systemd.template.service
*	заменить SITENAME, например, на staging.my-domain.com

## Структура папок:
Если допустить, что есть учетная запись пользователя в /home/username
/home/username

└── sites<br>
    └── SITENAME
        ├── database
        ├── source
        ├── static
        └── virtualenv

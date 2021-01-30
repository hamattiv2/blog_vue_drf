FROM nginx:1.11.7

# 設定ファイル
COPY ./nginx/nginx.conf /etc/nginx/nginx.conf
COPY ./nginx/default.conf /etc/nginx/sites-available/default
COPY ./nginx/default.conf /etc/nginx/sites-enabled/default
COPY ./nginx/uwsgi_params /etc/nginx/uwsgi_params

RUN mkdir /var/www && mkdir /var/www/front && mkdir /var/www/static

# Blog
簡易的なブログ

# 動かし方
ターミナルを2つ用意する

ターミナル1つ目
```
git clone https://github.com/hamattiv2/blog_vue_drf.git
cd blog_vue_drf
docker-compose up -d
docker-compose exec front sh
npm install --no-optional
npm run serve
```

ターミナル2つ目(コンテナ起動後)
```
docker-compose exec back uwsgi --socket :8001 --module config.wsgi
```

上記準備ができたら`http://localhost:8080/`にアクセスする。
デフォルトで4件分の記事が入っていますが、追加したい場合はadmin画面から追加してください。

adminユーザーの追加方法
```
docker-compose exec back bash 
python manage.py createsuperuser
```

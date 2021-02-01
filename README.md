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
npm run serve
```

ターミナル2つ目(コンテナ起動後)
```
docker-compose exec back uwsgi --socket :8001 --module config.wsgi
```

上記準備ができたら`http://localhost:8080/`にアクセスする。

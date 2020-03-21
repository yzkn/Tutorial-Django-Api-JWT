# Tutorial-Django-Api-JWT

---

[YA-androidapp/Tutorial-Django](https://github.com/YA-androidapp/Tutorial-Django) から引き続き、JWT を利用した API 認証を設定

## git clone

```ps
$ git clone https://github.com/YA-androidapp/Tutorial-Django-Api-JWT
```

## パッケージをインストール

```ps
$ cd C:\Users\y\Documents\GitHub\Tutorial-Django-Api-JWT
$ .\djangoenv\Scripts\activate
$ py -m pip install
```

## (Option) DB を初期化

```ps
$ cd C:\Users\y\Documents\GitHub\Tutorial-Django-Api-JWT\myproj
$ py manage.py makemigrations
$ py manage.py migrate
```

## 管理ユーザーを作成

```ps
$ py manage.py createsuperuser
Username (leave blank to use 'y'): y
Email address: y@example.net
Password:
Password (again):
Superuser created successfully.
```

## 動作確認

```ps
$ cd C:\Users\y\Documents\GitHub\Tutorial-Django-Api-JWT\myproj
$ py manage.py runserver
```

[http://127.0.0.1:8000/](http://127.0.0.1:8000/)にアクセスして、認証後アイテム一覧画面にアクセスできることを確認する

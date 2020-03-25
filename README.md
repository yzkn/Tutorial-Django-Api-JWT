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

### 既存の DB を初期化する場合

```ps
$ cd C:\Users\y\Documents\GitHub\Tutorial-Django-Api-JWT\myproj
$ py manage.py migrate --fake myapp zero
$ find . -path "myapp/migrations/*.py" -not -name "__init__.py" -delete
$ find . -path "myapp/migrations/*.pyc" -delete
$ py manage.py makemigrations
$ py manage.py sqlmigrate myapp 0001

DBサーバ上で、 `myapp_item` と `myapp_subitem` テーブルを削除

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

- [http://127.0.0.1:8000/](http://127.0.0.1:8000/)にアクセスして、認証後アイテム一覧画面にアクセスできることを確認する
- POST [http://127.0.0.1:8000/myapi/auth/jwt/create](http://127.0.0.1:8000/myapi/auth/jwt/create)にアクセスして、トークンを取得できることを確認する

Request

```json
Accept: application/json
Content-Type: application/json

{
  "username": "<USERNAME>",
  "password": "<PASSWORD>"
}
```

Response

```json
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOi**********.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU4NTI2NDUwNywianRpIjoiNjIwMTQ2MDViNWNjNDY3Yzk1MTRjZmRiNTUwYzllYzUiLCJ1c2Vy**********.C7l0oHS9lVym-X0Xe168sK7ARhgt2FQpM**********",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOi**********.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTg1MTgxNzA3LCJqdGkiOiI2NDY4ZmNiM2M5ZmE0NDBkYWQ1NjM5YmY5MTkwNDUzMSIsInVzZ**********.jgCyWD2w6vdvTrXWfI-mTFBIROwr5Ashe**********"
}
```

- GET [http://127.0.0.1:8000/myapi/item](http://127.0.0.1:8000/myapi/item)にアクセスして、レコード一覧を取得できることを確認する

Request

```json
Authorization: JWT <上の手順で取得したaccessトークン>
```

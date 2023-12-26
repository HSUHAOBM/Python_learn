```
1.get a token
POST /auth
Content-Type: application/json
body
{
  "username": "user1",
  "password": "abcxyz"
}

2.use
GET /protected
Authorization JWT <token>

```


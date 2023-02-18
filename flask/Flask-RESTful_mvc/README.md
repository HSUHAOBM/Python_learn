```
# Flask-RESTful
# windows
# POST
curl -i -H "Content-Type: application/json" -X POST -d "{\"name\":\"Jane Doe\",\"email\":\"jane.doe@example.com\"}" http://127.0.0.1:5000/users

# PUT
curl -i -H "Content-Type: application/json" -X PUT -d "{\"name\":\"Jane Doe\",\"email\":\"jane123.doe@example.com\"}" http://127.0.0.1:5000/users/1

# DELETE
curl -i -X DELETE http://localhost:5000/users/1

# POST
curl -i -H 'Content-Type: application/json' -X POST -d '{"name":"Jane Doe","email":"jane.doe@example.com"}' http://127.0.0.1:5000/users

# PUT
curl -i -H 'Content-Type: application/json' -X PUT -d '{"name":"Jane Doe","email":"jane123.doe@example.com"}' http://127.0.0.1:5000/users/1

# DELETE
curl -i -X DELETE http://localhost:5000/users/1

```


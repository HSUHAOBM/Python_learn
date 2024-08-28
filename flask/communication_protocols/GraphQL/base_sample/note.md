Postman 測試範例
```
Method: POST
URL: http://localhost:5000/graphql
Headers:
Content-Type: application/json
```

1. 查詢特定用戶

查詢 ID 為 123 的用戶資料。

```json
{
  "query": "query { user(id: 123) { id name gender order { product quantity price } } }"
}
```

2. 查詢所有用戶
查詢所有用戶資料。

```json
{
  "query": "query { all_users { id name gender order { product quantity price } } }"
}
```
3. 創建新用戶
創建一個名為 Alice，性別為 female 的用戶。

```json
{
  "query": "mutation { create_user(name: \"Alice\", gender: \"female\") { user { id name gender } } }"
}
```

4. 更新用戶資料
將 ID 為 123 的用戶名稱更新為 Robert。
```json
{
  "query": "mutation { update_user(id: 123, name: \"Robert\") { user { id name gender } } }"
}```
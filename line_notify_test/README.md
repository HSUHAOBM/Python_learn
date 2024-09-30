# LINE Notify Integration with Flask

這是一個簡單的 Flask 應用程式，實現了 LINE Notify OAuth2 的授權流程，讓使用者能夠授權後透過 LINE Notify 發送通知。

## 環境需求

- Flask
- requests

## 步驟



1. 在 LINE Notify [官方網站](https://notify-bot.line.me/my/services/) 註冊應用，並取得 `client_id` 和 `client_secret`。

2. 更新 `app.py` 中的設定：

    - `LINE_NOTIFY_CLIENT_ID`：你的應用的 `client_id`
    - `LINE_NOTIFY_CLIENT_SECRET`：你的應用的 `client_secret`
    - `LINE_NOTIFY_REDIRECT_URI`：設定成你的應用的回調 URL


6. 使用瀏覽器進入你的應用首頁，將會自動重導到 LINE Notify 的授權頁面。

7. 授權成功後，你將會看到「LINE Notify 綁定成功！」的訊息。

8. 發送通知測試，瀏覽至 `/notify`，應會收到 LINE Notify 發送的測試訊息。



## 授權與發送流程

1. 使用者訪問 `/` 會被重定向到 LINE Notify 的授權頁面。
2. 授權後，LINE 會將用戶重定向到 `/callback`，並附帶授權碼。
3. 使用授權碼換取 Access Token 並暫存於 session。
4. 用戶可以通過訪問 `/notify` 測試發送 LINE Notify 通知。

## 其他
- Access Token 暫時保存在 session 中，建議實際應用中將其存入資料庫。
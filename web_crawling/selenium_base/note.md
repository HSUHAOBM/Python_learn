element_to_be_clickable 用於確保某個元素已經在頁面上。
presence_of_element_located 用於確保某個元素可見且可被點擊
visibility_of_element_located 等待元素變得可見


# 安裝套件

```
pip install -U selenium
pip install webdriver-manager
```

## 相關參數

options.add_argument("--headless")：
解釋：以無頭模式運行 Chrome 瀏覽器，即不顯示瀏覽器的 GUI 界面。這對於自動化測試或在無圖形界面的環境（如服務器）中運行非常有用。
用途：節省系統資源，避免打開實際的瀏覽器窗口。

options.add_argument("--disable-gpu")：
解釋：禁用 GPU 硬件加速。
用途：在某些系統上，無頭模式下 GPU 硬件加速可能會導致問題，因此禁用它可以提高穩定性。

options.add_argument("--disable-extensions")：
解釋：禁用所有已安裝的 Chrome 擴展。
用途：避免已安裝的擴展影響自動化測試的結果，確保測試環境的一致性。

options.add_argument("--disable-infobars")：
解釋：禁用 "Chrome is being controlled by automated test software" 信息欄。
用途：避免這個提示信息影響測試的進行或干擾屏幕截圖。

options.add_argument("--start-maximized")：
解釋：啟動時將瀏覽器窗口最大化。
用途：確保瀏覽器以最大化狀態運行，這樣可以避免分辨率或窗口大小影響測試結果。

options.add_argument("--disable-notifications")：
解釋：禁用網站通知。
用途：避免網站彈出通知干擾自動化測試。

options.add_argument('--no-sandbox')：
解釋：禁用 Chrome 沙箱模式。
用途：在某些環境中，沙箱模式可能會導致問題，因此禁用它可以提高穩定性。注意，禁用沙箱模式會降低安全性，僅在必要時使用。

options.add_argument('--disable-dev-shm-usage')：
解釋：禁用 /dev/shm 共享內存使用。
用途：在容器化環境（如 Docker）中，默認的 /dev/shm 大小可能不足，導致 Chrome 崩潰，禁用此選項可以解決這個問題。
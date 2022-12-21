TCP/IP 的模型共有以下四層

Application Layer（應用層）
Transport Layer（傳輸層）
Internet Layer（網際網路層、網路層）
Network Access Layer（網路存取層）

應用層- 瀏覽網站的協定 HTTP 就是屬於應用層，網站遵守http 的各方面規範
傳輸層- 就是專門處理連線的穩定性，例如重送的機制
網路層- 負責把訊息定義網路上的地址
網路存取層- 網路卡中的 MAC Address 就是基於這個協定的


OSI 七層

Application Layer（應用層）
Presentation Layer（表達層）
Session Layer（會議層）
Transport Layer（傳輸層）
Network Layer（網路層）
Data Link Layer（資料連結層）
Physical Layer（實體層）


表達層，規範數據的傳送與接收格式，例如使用 ASCII 還是 UTF-8 來編碼
會議層，規範一次會議（兩者間的連線）的機制，例如做身分認證、會議的重新連線等等
實體層，規範了通訊設備間的通訊規格，例如電壓、傳輸媒介（線材、連接方式）
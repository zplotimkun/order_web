# 前置步驟

1. 使用 Powershell 在資料夾中建立虛擬環境
- python -m venv venv
2. 進入虛擬環境
- .\venv\Scripts\activate
3. 下載套件
- pip install -r .\requirements.txt
4. 將 .html 檔案放入 .\order_web\order_app\templates\
5. 重新命名 .html 檔案為 index.html
6. 進入 order_web 資料夾
7. 啟動 server
- python manage.py runserver

開啟 Chrome 進入 127.0.0.1:8000


# Files

```mermaid
graph LR
A[order_web] --> B(order_web)
A --> requirements((requirements.txt))
B --> C(order_app)
B --> D(order_web)
B --> py{manage.py}
C --> E(templates)
E --> html{index.html}

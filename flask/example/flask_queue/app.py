from flask import Flask, render_template, request, jsonify
from queue import Queue
import time
import threading

app = Flask(__name__)

# 初始化一個隊列
queue = Queue()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/check_queue")
def check_queue():
    print('queue',queue.__dict__)
    return "check cmd~"

@app.route("/use_queue")
def use_queue():
    if queue.qsize() > 0:

        user, start_time = queue.get()
        # time.sleep(10)
        # 處理完成後，返回結果
        result = {"user": user, "wait_time": int((time.time() - start_time) / 60)}
        print(result)
        return jsonify(result)
    else:
        return "無人排隊"

@app.route("/ticket", methods=["POST"])
def ticket():
    # 接收用戶提交的排隊請求
    user = request.form.get("user")
    start_time = time.time()
    # 將排隊請求加入到隊列中
    queue.put((user, start_time))
    # 返回排隊狀態頁面，讓用戶可以查看自己的排隊狀態
    return render_template("status.html", user=user)

@app.route("/status/<user>")
def status(user):
    # 查找用戶在隊列中的位置和預計等待時間
    position = None
    wait_time = None
    wait_time_after = None

    queue_length = len(queue.queue)

    for i, item in enumerate(queue.queue):
        print(i,item)
        if item[0] == user:
            position = i + 1
            # 已等待時間
            wait_time_after = int((time.time() - item[1]) / 60)
            # 預計等待時間
            wait_time = int(queue_length * 1)
            break
    # 返回用戶的排隊狀態
    return jsonify({
        "user": user,
        "position": position,
        "wait_time": wait_time,
        "wait_time_after": wait_time_after
    })

# 定期處理隊列中的排隊請求
def process_queue():
    while True:
        # time.sleep(5)
        # print('===========================')
        # print(queue.qsize())
        # print(len(queue.queue))
        # print('===========================')

        if queue.qsize() > 0:
            print('開始處理排隊')
            # 取出隊列頂部的排隊請求，進行處理
            user, start_time = queue.get()
            time.sleep(60)
            # 處理完成後，返回結果
            result = {"user": user, "wait_time": int((time.time() - start_time) / 60)}
            print(result)


if __name__ == '__main__':
    # use thread
    scheduler_thread = threading.Thread(target=process_queue, daemon=True)
    scheduler_thread.start()

    # 啟動Flask應用程序
    app.run(debug=True)
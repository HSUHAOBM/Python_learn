from flask import Flask, render_template, request, jsonify, session, redirect, url_for

from queue import Queue
import time
import threading

app = Flask(__name__)

# 初始化一個隊列
queue = Queue()
app.secret_key = "7779keytest"


@app.route("/")
def index():
    return render_template("index.html")


# 查看
@app.route("/check_queue")
def check_queue():
    print('queue', queue.__dict__)
    queue_info = {
        "queue_length": queue.qsize(),
        "queue_items": list(queue.queue)
    }
    return jsonify(queue_info)


# 取出隊伍第一個
@app.route("/use_queue")
def use_queue():
    if queue.qsize() > 0:
        user, start_time = queue.get()
        # 處理完成後，返回結果
        result = {"user": user, "wait_time": int(
            (time.time() - start_time) / 60)}
        print(result)
        return jsonify(result)
    else:
        return "無人排隊"


@app.route("/ticket", methods=["POST"])
def ticket():
    # 接收用戶提交的排隊請求
    user = request.form.get("user")

    # 检查用户是否已经在队列中
    for item in queue.queue:
        if item[0] == user:
            return "您已在排請勿重複"

    start_time = time.time()
    # 將排隊請求加入到隊列中
    queue.put((user, start_time))
    session['is_queued'] = True

    # 返回排隊狀態頁面，讓用戶可以查看自己的排隊狀態
    return render_template("status.html", user=user)


@app.route("/status/<user>")
def status(user):
    if not queue.empty():
        # 查找用戶在隊列中的位置和預計等待時間
        position = None
        wait_time = None
        wait_time_after = None

        queue_length = len(queue.queue)

        for i, item in enumerate(queue.queue):
            print(i, item)
            if item[0] == user:
                position = i + 1
                # 已等待時間
                wait_time_after = int((time.time() - item[1]) / 60)
                # 預計等待時間
                wait_time = int(queue_length * 1)
                # 返回用戶的排隊狀態
                return jsonify({
                    "in_queue": True,
                    "user": user,
                    "position": position,
                    "wait_time": wait_time,
                    "wait_time_after": wait_time_after
                })
    else:
        return jsonify({
            "in_queue": False,
        })


# 排隊後畫面,簡單用 session判斷是否有排隊
@app.route("/start_page")
def start_page():
    if session.get('is_queued'):
        return "Welcome to start_page page! (from queue)"
    else:
        return redirect(url_for('index'))


# 定期處理隊列中的排隊請求
def process_queue():
    while True:
        print("")
        print("--監控排隊-- 列隊長度：", queue.qsize())

        time.sleep(60)
        # print('===========================')
        # print(queue.qsize())
        # print(len(queue.queue))
        # print('===========================')

        if queue.qsize() > 0:
            print("隊伍有人,取出第一順位")
            # 取出隊列頂部的排隊請求，進行處理
            user, start_time = queue.get()
            # 處理完成後，返回結果
            result = {"user": user, "wait_time": int(
                (time.time() - start_time) / 60)}
            print("結束排隊", result)
        else:
            print("隊伍目前是空")


if __name__ == '__main__':
    # use thread
    # 正式環境 flask debug=False , 避免起2次
    scheduler_thread = threading.Thread(target=process_queue, daemon=True)
    scheduler_thread.start()

    # 啟動Flask應用程序
    # app.run(debug=True)
    app.run(debug=False)

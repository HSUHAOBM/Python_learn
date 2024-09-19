import pika

# 1. 建立連結
credentials = pika.PlainCredentials('celery', 'password123')
parameters = pika.ConnectionParameters(host='localhost',
                                       virtual_host='my_vhost',
                                       credentials=credentials)
connection = pika.BlockingConnection(parameters)

# 2. 實作channel
channel = connection.channel()

# 3. 建立隊列
channel.queue_declare(queue='queue_name')

# 4. 設置callback


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    # print("Channel ID: %s" % ch)
    # print("Exchange: %s" % method.exchange)
    # print("Routing Key: %s" % method.routing_key)


# 接收訊息
channel.basic_consume(on_message_callback=callback,
                      queue='queue_name',)

print(' [*] Waiting for messages. To exit press CTRL+C')

# 開始接收
try:
    channel.start_consuming()
except KeyboardInterrupt:
    # 使用者按下 CTRL+C 時關閉連接
    connection.close()

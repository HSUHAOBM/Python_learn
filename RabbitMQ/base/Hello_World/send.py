import pika

# 1. 建立連結
credentials = pika.PlainCredentials('celery', 'password123')
parameters = pika.ConnectionParameters(host='localhost',
                                       virtual_host='my_vhost',
                                       credentials=credentials)
connection = pika.BlockingConnection(parameters)
#  2. 實作channel
channel = connection.channel()
#  3. 建立隊列
channel.queue_declare(queue='queue_name')
#  4. 發送訊息
channel.basic_publish(exchange='',
                      routing_key='queue_name',
                      body='Hello World!')
#  5. 單純列印訊息方便檢視
print(" [x] Sent 'Hello World!'")
#  6. 釋放資源，關閉連結
connection.close()

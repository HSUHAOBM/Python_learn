import pika
import sys

credentials = pika.PlainCredentials('celery', 'password123')
parameters = pika.ConnectionParameters(host='localhost',
                                       virtual_host='my_vhost',
                                       credentials=credentials)
connection = pika.BlockingConnection(parameters)

channel = connection.channel()

# channel.queue_delete(queue='hello')
channel.queue_declare(queue='task_queue', durable=True)

# 設置參數接收外部呼叫程式時傳入的字串
# python new_task.py {message}
message = ''.join(sys.argv[1:]) or 'Hello World!'

channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(delivery_mode=2))

print(" [x] Sent % (message,)")

connection.close()

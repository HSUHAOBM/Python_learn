import pika
import time

credentials = pika.PlainCredentials('celery', 'password123')
parameters = pika.ConnectionParameters(host='localhost',
                                       virtual_host='my_vhost',
                                       credentials=credentials)
connection = pika.BlockingConnection(parameters)

channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)


def callback(ch, method, properties, body):
    print(" [x] Received %r" % (body, ))

    # time.sleep(body.count(b'.'))
    time.sleep(10)
    print(" [x] Done")
    # ch.basic_ack(delivery_tag=method.delivery_tag)


# 預設為公平調度
# Consumer每次只會執行一個工作:只接收一條未確認的消息
# channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_message_callback=callback,
                      queue='task_queue',)


print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

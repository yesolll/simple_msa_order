import pika

params = pika.URLParameters('amqps://lswqptek:8pKYJcfazSYR1f9fygl5Rb4CE9b6i61j@dingo.rmq.cloudamqp.com/lswqptek')
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='order')
# 여러 큐가 있을 수 있다. 그 중 order로 보낸 것만 받겠다 선언()
# 자기 자신이지만 실습 위해 우선1 개념파악

def callback(dh, method, properties, body):
    print('Received in order')
    print(body)

channel.basic_consume(queue='order', on_message_callback=callback)

print('Started consuming')

channel.start_consuming()

print('close consuming')

channel.close()
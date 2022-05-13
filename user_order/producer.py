import pika

params = pika.URLParameters('amqps://lswqptek:8pKYJcfazSYR1f9fygl5Rb4CE9b6i61j@dingo.rmq.cloudamqp.com/lswqptek')
connection = pika.BlockingConnection(params)
channel = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='order', body='hello!!')
    # body를 routing_key로 전달하겠다. (~>consumer)
#This scripts explains the connection of rabbitmq to send the result message

import pika ,time, random, traceback, datetime, json, sys, os 

parametres = "amqp://admin:mypass@rabbit//"
#url = os.environ["amqp://rabbit_mq?connection_attempts=10&retry_delay=10"]
url_parameters = pika.URLParameters(parametres)
connection = pika.BlockingConnection(url_parameters)
channel = connection.channel()

def generate_data_rabbitmq_server(delay : int) -> (None):
    next_time = time.time() + delay
    while True:
        time.sleep(max(0, next_time - time.time()))
        try:
            current_datetime = datetime.datetime.now()
            current_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
            data1 = round(random.uniform(0, 10), 2)
            data2 = round(random.uniform(0, 10), 2)
        except Exception:
            traceback.print_exc()

        publish_message = {"timedate": current_datetime, "value1" : data1, "value2" : data2}

        channel.queue_declare(queue='generated_data')
        channel.basic_publish(exchange='', routing_key='generated_data', body=json.dumps(publish_message))

        next_time += (time.time() - next_time) // delay * delay + delay
        print(publish_message)

        # count += 1
        # if count == 30:
        #     break

        print(" *** The result sent to the RabbitMQ client  Task A ---> B *** ")

        # connection.close()


if __name__ == '__main__':
    try:
        generate_data_rabbitmq_server(1)
    except KeyboardInterrupt:
        print('Interrupted by press keyboard key')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
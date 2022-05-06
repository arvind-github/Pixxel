import pika, sys, os
import requests
import json
import ast

def main():
    #credentials = pika.PlainCredentials(username='myuser', password='password')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='10.25.215.42'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        # print(" [x] Received %r" % body)

        data =((body).decode("utf-8"))
        #data = ast.literal_eval(data)
        data = data.replace("'",'"').strip()

        headers = {'Content-type': 'application/json'}
        response = requests.post("http://machine_ip:8000/api/crud/", data=data, headers=headers)
        print(response.text)
        #response_body = response.json()
        #print(response_body["message"])
        #if response.status_code == 200:
        #    print("Data Added")

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

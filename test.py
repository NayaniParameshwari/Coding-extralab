import pika ,time, random, traceback, datetime, json, sys, os 

url = "amqp://guest:guest@localhost:5672/"
url_parameters = pika.URLParameters(url)
connection = pika.BlockingConnection(url_parameters)
channel = connection.channel()
print("success")
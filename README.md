# coding-execise

Develop a small infrastructure composed of 5 docker containers. Each uses a
different service.

Task :
A Is a python script that produces an object of random data every 1 second.
Then it pushes that object in B the message broker.
The B2 container must read the B queue and insert the produced data in a C
database.
The D is a REST API that exposes 3 GET routes.

Solution:

Introduction:
A-First i produce the random data
B- Then i pushed the random data to mysql database using message broker (Rabbitmq).
In the messagebroker rabbimq they are several methods i used Fanout method, which is send
message by the matching exchange.
C-Then i wrote the another script which receives the rabbitmq message and sends data to
mysql.
In additional i developed a small interface using Streamlit, which represents all the data in
details.

Stack technique :
Backend: Rabbitmq, mysql, flask
Frontend: Streamlit
Processing : Python

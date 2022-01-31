### Simple Notification

A basic & minimal example, of handling notification using websocket.

### Tools

- [Django 3.1](https://djangoproject.com)
- [Channels 3.0.1](https://channels.readthedocs.io/en/stable/)

### Installation

On your terminal/shell

```bash

pip3 install -r requirements.txt

sudo docker run -p 6379:6379 -d redis:5

./manage.py runserver

```

# How notification system should work.

## **Common HTTP endpoint**

---

- ### `/notification/unread`

  HTTP endpoint, shows unread notifications with unread count

- ### `/notification/all`

  HTTP endpoint, shows all notifications

## **First implementation using channels**

---

- ### `ws/notification/receiver`

  WS endpoint, shows new notifications/

## **Second implementation using websockets (python package)**

---

- ### `ws/notification/receiver`

  WS endpoint, shows new notifications/

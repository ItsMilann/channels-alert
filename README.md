### Simple Notification

A basic & minimal example, of handling notification using websocket.

### Tools

- [Django 3.1](https://djangoproject.com)
- [Channels 3.0.1](https://channels.readthedocs.io/en/stable/)

### Installation

On your terminal/shell

```bash

pip3 install ibalert

sudo docker run -p 6379:6379 -d redis:5

```

### Quiz setup

---

In your project's settings.py file. Add ibalert and channels to intallled apps and configure redis.

```python
# settings.py

INSTALLED_APPS = [
  ...,
  "ibalert",
  "channels"
]

ASGI_APPLICATION = "ibalert.asgi.application"

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {"hosts": [("localhost", 6379)]},
    }
}

```

In your project's urls.py

```python
...
from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html")),
    ...
]
```

In your templates directory add home.html file. (Just to make sure the app is working. Later you can implement it the way you want.)

```html
<html>
  <head>
    <title>IB-Alert</title>
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"
      rel="stylesheet"
    />
  </head>

  <body>
    <div class="container">
      <h4 class="text-center">
        Notifications
        <span class="badge bg-danger" id="counter">0</span>
      </h4>

      <ul id="notifylist"></ul>
    </div>
  </body>
  <script>
    const webSocket = new WebSocket("ws://localhost:8000/notifications/")
    webSocket.onclose = function (e) {
      console.error("Chat socket closed unexpectedly")
    }
    webSocket.onopen = function (e) {
      webSocket.send(JSON.stringify({ userID: 1 }))
    }
    webSocket.onmessage = function (action) {
      const data = JSON.parse(action.data)
      console.log(data.event == "Notification", data)
      const nl = document.querySelector("#notifylist")
      if (data.event == "Notification") {
        var counter = document.getElementById("counter")
        counter.innerText = data.unread_count
        var el = document.createElement("li")
        el.innerHTML = `<b>New Notification </b>: ${data.text}!`
        nl.appendChild(el)
      }
    }
  </script>
</html>
```

Now make migrations, migrate, **createsuperuser** and runserver. You should see something like below.

```bash
starting ASGI/Channels version 3.0.4 development server at http://127.0.0.1:8000/
```

Open django shell `python3 manage.py shell` along with open `http://127.0.0.1:8000` on a browser. And run the following on your django shell.

```bash
from ibalert.models import Notifications
Notificatons.objects.create(text='hello there!', user_id=1)
```

You should see new notification on your browser.

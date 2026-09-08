

class Notification:
    def send(self, message):
        print(f"Sending notification: {message}")

class Email(Notification):
    def send(self, message):
        print(f"sending Email: {message}")

class SMS(Notification):
    def send(self, message):
        print(f"sending SMS: {message}")

class Watsapp(Notification):
    def send(self, message):
        print(f"sending Watsapp: {message}")

notifications = [Email(), SMS(), Watsapp()]

for notification in notifications:
    notification.send("Hello, your order has been shipped!")
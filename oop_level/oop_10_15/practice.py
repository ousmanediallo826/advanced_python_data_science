#=============================Exercise: The E-Commerce Notification Pipeline==========================
class Notification:
    def send(self, message):
        print(f"Notification base tracking: {message} logged permanently.")


class EmailNotification(Notification):
    def send(self, message):
        print(f"[Email Dispatch]: Sending email containing -> {message}")
        super().send(message)

class SMSNotification(Notification):
    def send(self, message):
        print(f"[SMS Dispatch]: Sending text alert containing -> {message}")
        super().send(message)

class CustomerAlertSystem(EmailNotification, SMSNotification):
    def send(self, message):
        print(f"[Customer Dispatch]: Sending email containing -> {message}")
        super().send(message)

alert_pipeline = CustomerAlertSystem()
alert_pipeline.send("Your order #10492 has been shipped!")



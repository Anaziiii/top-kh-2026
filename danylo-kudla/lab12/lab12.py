from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

class SMS(Notification):
    def send(self, message):
        print(f"Відправка SMS: {message}")

class Telegram(Notification):
    def send(self, message):
        print(f"Відправка Telegram: {message}")

class NotificationSend(ABC):
    @abstractmethod
    def create_notification(self):
        pass

    def notify_user(self, massage):
        notification = self.create_notification()
        notification.send(massage)

class SMSSender(NotificationSend):
    def create_notification(self):
        return SMS()

class TelegramSender(NotificationSend):
    def create_notification(self):
        return Telegram()

def client_business_logic(sender, message):
    sender.notify_user(message)

telegram_sender = TelegramSender()
client_business_logic(telegram_sender, "Ваше замовлення прийнято!")

sms_sender = SMSSender()
client_business_logic(sms_sender, "Ваш код підтвердження: 1234")
# Liskov Substitution Principle (LSP) 里氏替換原則
# 繼承子類別 父類別不受影響

from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def notify(self, message, email):
        pass


class Email(Notification):
    def notify(self, message, email):
        print(f'Send {message} to {email}')


class SMS(Notification):
    def notify(self, message, phone):
        print(f'Send {message} to {phone}')


if __name__ == '__main__':
    notification = SMS()
    notification.notify('Hello', 'john@test.com')


# SMS not use email
# ------------------------------------------------------------------------

from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def notify(self, message):
        pass


class Email(Notification):
    def __init__(self, email):
        self.email = email

    def notify(self, message):
        print(f'Send "{message}" to {self.email}')


class SMS(Notification):
    def __init__(self, phone):
        self.phone = phone

    def notify(self, message):
        print(f'Send "{message}" to {self.phone}')


class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


class NotificationManager:
    def __init__(self, notification):
        self.notification = notification

    def send(self, message):
        self.notification.notify(message)


if __name__ == '__main__':
    contact = Contact('John Doe', 'john@test.com', '(408)-888-9999')

    sms_notification = SMS(contact.phone)
    email_notification = Email(contact.email)

    print('sms_notification',sms_notification.__dict__)  # SMS object {'phone': '(408)-888-9999'}
    print('email_notification',email_notification.__dict__) # Email object {'email': 'john@test.com'}

    notification_manager = NotificationManager(sms_notification)
    notification_manager.send('Hello John')

    # notification_manager.notification = email_notification
    notification_manager = NotificationManager(email_notification)
    notification_manager.send('Hi John')
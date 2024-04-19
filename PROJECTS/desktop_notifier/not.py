from plyer import notification
import time

if __name__ == '__main__':
    while True:
            notification.notify(
                    title="Notification", 
                    message="this is notification testing",
                    app_icon="icon.png",
                    timeout=5)
            time.sleep(10)
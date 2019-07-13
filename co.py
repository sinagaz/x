import threading
def send_email(): print("email sent!")

t = threading.Timer(12, send_email)
t.start()
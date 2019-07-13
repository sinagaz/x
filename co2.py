import threading
def send_email(): print("email sent!")

t = threading.Timer(2, send_email)
t.start()
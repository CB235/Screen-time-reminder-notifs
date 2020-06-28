from win10toast import ToastNotifier
import time
toaster = ToastNotifier()
def msg():
    toaster.show_toast("Eye break!","20/20/20")

while True:
    msg()
    time.sleep(1200)
    

##install win10toast with the command "pip install win10toast"


from win10toast import ToastNotifier
import time
toaster = ToastNotifier()
def msg():
    toaster.show_toast("Eye break!","Take a quick break!")

while True:
    msg()
    time.sleep(1200)
    

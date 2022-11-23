import watson
from datetime import datetime
from gi.repository import Notify

# List of weekdays when reminder should be active.
# Monday = 0
WORKING_DAYS = [0, 1, 2, 3, 4] 
START_HOUR = 8
END_HOUR = 18

def send_notification(msg):
    Notify.init("Watson Reminder")
    notification = Notify.Notification.new ("Watson", msg,)
    notification.set_timeout(0)
    notification.show()

def watson_active():
    w = watson.utils.create_watson()
    return w.is_started

CUR = datetime.now()

if (
    CUR.weekday() in WORKING_DAYS and 
    CUR.hour in range(START_HOUR, END_HOUR) and
    not watson_active()
):
    send_notification("Shouldn't you be tracking something?")

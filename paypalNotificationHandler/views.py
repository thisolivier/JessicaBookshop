from paypalNotificationHandler import flaskInstance

@flaskInstance.route('/')
def hello():
    return 'I am Jessica Robot!'
import paypalNotificationHandler.interface.flaskIsRunning as flaskIsRunning
import paypalNotificationHandler.paypal.paypal as paypal

from flask import request

from paypalNotificationHandler import flaskInstance

@flaskInstance.route('/')
def root():
    return flaskIsRunning.flaskIsRunning()

@flaskInstance.route('/paypal/ipn', methods=['POST'])
def paypalIPN():
    return paypal.receive_IPN_request(request)
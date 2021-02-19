from flask import Flask
flaskInstance = Flask(__name__)

import paypalNotificationHandler.views
import paypalNotificationHandler.paypal
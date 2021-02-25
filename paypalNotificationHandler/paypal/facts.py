
from paypalNotificationHandler import flaskInstance

flaskInstance.config['PAYPAL_LIVE'] = False

PAYPAL_LIVE_URL = 'https://ipnpb.paypal.com/cgi-bin/webscr'
PAYPAL_SANDBOX_URL = 'https://ipnpb.sandbox.paypal.com/cgi-bin/webscr'
PAYPAL_URL = PAYPAL_LIVE_URL if flaskInstance.config['PAYPAL_LIVE'] else PAYPAL_SANDBOX_URL
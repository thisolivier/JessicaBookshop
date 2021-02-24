import urllib
import sys
# TODO: Use eventlet, http://eventlet.net/doc/examples.html
# Also, use pypy when running

from flask import request

from paypalNotificationHandler import flaskInstance

flaskInstance.config['PAYPAL_LIVE'] = False

PAYPAL_LIVE_URL = 'https://ipnpb.paypal.com/cgi-bin/webscr'
PAYPAL_SANDBOX_URL = 'https://ipnpb.sandbox.paypal.com/cgi-bin/webscr'

PAYPAL_URL = PAYPAL_LIVE_URL if flaskInstance.config['PAYPAL_LIVE'] else PAYPAL_SANDBOX_URL

# helper function to verify ipn message
# adds verification string and asks paypal if it sent us this message
# checks response for valid or invalid state (note, blocking)
def verify_IPN_with_paypal(ipn_data: str) -> bool:
    # NEXT TODO: Fix this logic, it's bust
    # - what the fuck is that request.data
    verification_string = 'cmd=_notify-validate&%s' % ipn_data
    print("verification string...", verification_string)
    response = urllib.request.urlopen(PAYPAL_URL, data=verification_string.encode())
    responseBody = response.read().decode('utf-8')
    if responseBody == 'INVALID':
        return False
    elif response == 'VERIFIED':
        return True
    else:
        print("The reponse body was", responseBody)
        raise Exception('Reponse cannot be decoded')

def handle_authentic_IPN(ipn_request):
    print("We got an IPN!", ipn_request.form)
    sys.stdout.flush()

@flaskInstance.route('/paypal/ipn', methods=['POST'])
def handleIPN():

    ipn_authentic = False
    print("data", request.data)
    print("form", request.form)
    print("args", request.args)
    try:
        ipn_authentic = verify_IPN_with_paypal(request.data)
    except:
        print("paypalNotificationHander:paypal:40 - failed to get a response from paypal")
        sys.stdout.flush()
        return "Could not communicate with paypal to verify that message", 403

    if ipn_authentic:
        handle_authentic_IPN(request)
        return "Joyous times human, IPN message validated by PayPal", 200
    else:
        print("paypalNotificationHander:paypal:40 - got an invalid response from paypal")
        sys.stdout.flush()
        return "Paypal said your message wasn't from them, stranger thing...", 403
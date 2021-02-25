import urllib
# TODO: Use eventlet, http://eventlet.net/doc/examples.html
# Also, use pypy when running

import paypalNotificationHandler.logger as logger
import paypalNotificationHandler.paypal.facts as facts

from flask import request

# adds verification string and asks paypal if they sent us this IPN
# checks response for valid or invalid state (note, blocking)
def verify_IPN_with_paypal(ipn_data: str) -> bool:

    verification_string = 'cmd=_notify-validate&%s' % ipn_data
    logger.makeNote("verification string...", verification_string)
    response = urllib.request.urlopen(facts.PAYPAL_URL, data=verification_string.encode())
    responseBody = response.read().decode('utf-8')
    if responseBody == 'INVALID':
        return False
    elif responseBody == 'VERIFIED':
        return True
    else:
        print("The reponse body was", responseBody)
        raise Exception('Reponse cannot be decoded')
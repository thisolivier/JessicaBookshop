from typing import Tuple

import urllib
# TODO: Use eventlet, http://eventlet.net/doc/examples.html
# Also, use pypy when running

import paypalNotificationHandler.logger as logger
import paypalNotificationHandler.paypal.handleHandshakeSuccess as handle_handshake_success
import paypalNotificationHandler.paypal.handshakeWithPaypal as handshake_with_paypal

from flask import request

# Responsible for deciding what to reply to the requester & sending off the request data for processing
def receive_IPN_request(request: request) -> Tuple[str, int]:
    
    ipn_authentic = False
    try:
        ipn_authentic = handshake_with_paypal.verify_IPN_with_paypal(request.get_data(True, True))
    except:
        logger.makeNote("paypalNotificationHander:paypal:40 - failed to get a response from paypal")
        return "Could not communicate with paypal to verify that message", 403

    if ipn_authentic:
        handle_handshake_success.handle_authentic_IPN(request.form)
        return "Joyous times human, IPN message validated by PayPal", 200
    else:
        logger.makeNote("paypalNotificationHander:paypal:40 - got an invalid response from paypal")
        return "Paypal said your message wasn't from them, stranger thing...", 403
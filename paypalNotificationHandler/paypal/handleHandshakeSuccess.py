import paypalNotificationHandler.logger as logger

def handle_authentic_IPN(ipn_request):
    logger.makeNote("We got an IPN!", ipn_request.form)
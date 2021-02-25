import paypalNotificationHandler.logger as logger

def handle_authentic_IPN(ipn_form):
    logger.makeNote("We got an IPN!", ipn_form)
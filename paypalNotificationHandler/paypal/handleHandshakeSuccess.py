import paypalNotificationHandler.logger as logger

def handle_authentic_IPN(ipn_form):
    logger.makeNote("We got an IPN!", ipn_form)
    # So, next step is to extract the data from the form and see if we have a order in play
    # I.E. can we initialise an order from the form?
    # Next we need to store the order & add it to a queue for sending
    # Or you can just call the sender directly, a queue would scale better, but we're not at scale
    # It would decouple things more...
    # Anyway, you then want an email sender which will take an order, a static template file and attachment location and send the email.
    # Finally, you want an interface where you can update the static template file and attachment
    # You should also be able to inspect the logs, and trigger a manual order
    # Access should be securely controlled


def payload(message, payload={}, status=200):
    return {"status":   status,
            "message":  message,
            "payload":  payload}


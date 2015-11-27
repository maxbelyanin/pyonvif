
ERR_ONVIF_UNKNOWN = 1


class ONVIFError(Exception):
    def __init__(self, err):
        self.reason = 'Unknown error: ' + str(err)
        self.code = ERR_ONVIF_UNKNOWN

    def __str__(self):
        return self.reason
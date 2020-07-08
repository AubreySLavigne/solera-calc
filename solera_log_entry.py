
class SoleraLogEntry:
    def __init__(self, **kw):
        self.date = kw.get('date')
        self.amount = kw.get('delta')
        self.desc = kw.get('desc')
        self.idvp_code = kw.get('idvp_code')


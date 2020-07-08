from solera_log_entry import SoleraLogEntry


class SoleraLog:
    def __init__(self):
        self.entries = []

    def __str__(self):
        return str(self.total())

    def add(self, **kw):
        delta = kw.get('delta')
        if delta == 0:
            return 0

        if delta > 0:
            self.entries.append(SoleraLogEntry(**kw))
        else:
            self.drink(delta)

    def drink(self, amount):
        total = self.total()
        for entry in self.entries:
            ratio = entry.amount / total
            delta = ratio * abs(amount)
            entry.amount -= delta

    def summary(self):
        res = []
        for entry in self.entries:
            res.append({
                'desc': entry.desc,
                'amount': entry.amount
            })
        return res

    def total(self):
        res = 0
        for entry in self.entries:
            res += entry.amount
        return res

import json


class Gen:
    def __init__(self, idpbi, value, estimation):
        self.idpbi = idpbi
        self.value = value
        self.estimation = estimation
        self.included = 0

    def __str__(self):
        return 'idpbi: '+str(self.idpbi)+', value: '+str(self.value)+', estimation: '+str(self.estimation)+', included: '+str(self.included)

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)

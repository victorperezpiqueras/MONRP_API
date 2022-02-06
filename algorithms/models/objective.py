class Objective:
	def __init__(self, value, minimize):
		self.value = value
		self.minimize=minimize

	def is_minimization(self):
		return self.minimize
	def toJson(self):
		return json.dumps(self, default=lambda o: o.__dict__)

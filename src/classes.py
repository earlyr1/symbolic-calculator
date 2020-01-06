import operator

class Operable:
	def __add__(self, rop):
		return Formula(operator.add, self, rop)

	def __radd__(self, lop):
		return Formula(operator.add, lop, self)

	def __sub__(self, rop):
		return Formula(operator.sub, self, rop)

	def __rsub__(self, lop):
		return Formula(operator.sub, lop, self)

	def __mul__(self, rop):
		return Formula(operator.mul, self, rop)

	def __rmul__(self, rop):
		return Formula(operator.mul, rop, self)

	def __truediv__(self, rop):
		return Formula(operator.truediv, self, rop)

	def __rtruediv__(self, lop):
		return Formula(operator.truediv, lop, self)

	def __floordiv__(self, rop):
		return Formula(operator.floordiv, self, rop)

	def __rfloordiv__(self, lop):
		return Formula(operator.floordiv, lop, self)

	def __mod__(self, rop):
		return Formula(operator.mod, self, rop)

	def __rmod__(self, lop):
		return Formula(operator.mod, lop, self)

	def __neg__(self):
		return Formula(operator.sub, 0, self)

	def __pow__(self, rop):
		return Formula(operator.pow, self, rop)

	def __rpow__(self, lop):
		return Formula(operator.pow, lop, self)


class Formula(Operable):
	def __init__(self, op, lop, rop=None):
		self.op = op
		self.lop = lop
		self.rop = rop
		self.varset = lop.varset + rop.varset

	def __call__(self, vardict):
		return self.op()


class Variable(Operable):
	def __init__(self, name):
		self.varset = {name,}

	def __call__(self, vardict):

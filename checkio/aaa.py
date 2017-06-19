def checkio(num):
	for i in range(2,37):
		try:
			if int(num,i) % (i -1) == 0:
				return i
		except ValueError as e: pass
	return 0

# print(checkio("18"))
# print(checkio("1010101011"))
# print(checkio("222"))
# print(checkio("A23B"))
# print(checkio("IDDQD"))


class Customer(object):
    """A customer of ABC Bank with a checking account. Customers have the
    following properties:

    Attributes:
        name: A string representing the customer's name.
        balance: A float tracking the current balance of the customer's account.
    """

    def __init__(self, name, balance=0.0):
        """Return a Customer object whose name is *name* and starting
        balance is *balance*."""
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        """Return the balance remaining after withdrawing *amount*
        dollars."""
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        """Return the balance remaining after depositing *amount*
        dollars."""
        self.balance += amount
        return self.balance


class Car(object):

    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model

    # @staticmethod
    def make_car_sound(self):
        print 'vroooooom'


from 
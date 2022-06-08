class PayPalPayment:
    def make_payment(self, amount):
        print("Payment of $ {} made from PayPal.".format(amount))


class BankAccountPayment:
    def make_payment(self, amount):
        print("Payment of $ {} made from bank account.".format(amount))


class Customer:
    def __init__(self, strategy):
        self._strategy = strategy

    def strategy(self):
        return self._strategy

    def do_some_business_logic(self, amount):
        self._strategy.make_payment(amount)


Customer(PayPalPayment()).do_some_business_logic(1000)

Customer(BankAccountPayment()).do_some_business_logic(2000)

#====================7. Magic Methods=============================

class Length:
    __metric = {
        "mm": 0.001, "cm": 0.01, "m": 1,
        "km": 1000, "in": 0.0254, "ft": 0.3048,
        "yd": 0.9144, "mi": 1609.344
    }

    def __init__(self, value, unit = "m"):
        self.value = value
        self.unit = unit

    def Converse2Meters(self):
        return self.value * Length.__metric[self.unit]

    def __add__(self, other):
        l = self.Converse2Meters() + other.Converse2Meters()
        return Length(l / Length.__metric[self.unit], self.unit)

    def __str__(self):
        return str(self.Converse2Meters())

    def __repr__(self):
        return "Length(" + str(self.value) + ", '" + self.unit + "')"



if __name__ == "__main__":
    x = Length(4)
    print(x)
    y = eval(repr(x))
    z = Length(4.5, "yd") + Length(1)
    print(repr(z))
    print(z)



#===========================8. Dynamic Data Transformation===========================

class Product:

    conversion_rates = {'USD': 1, 'EUR': 0.92, 'CHF': 0.90, 'GBP': 0.79}

    def __init__(self, name, price, shipping_cost, currency='USD'):
        self.name = name
        self._price = price
        self._shipping_cost = shipping_cost
        self.currency = currency
        self._used_currency = currency



    def set_currency(self, new_currency, adapt_data=False):
        if self.currency != new_currency:
            self.currency = new_currency
        if adapt_data:
            self._price = self.price
            self._shipping_cost = self.shipping_cost
            self._used_currency = new_currency

    @property
    def price(self):
        return self._convert_currency(self._price)

    @property
    def shipping_cost(self):
        return self._convert_currency(self._shipping_cost)

    def _convert_currency(self, amount):
        factor = Product.conversion_rates[self.currency] / Product.conversion_rates[self._used_currency]
        return round(amount * factor, 2)

    def __str__(self):
        return f"Product: {self.name}, Price: {self.price} {self.currency}, Shipping Cost: {self.shipping_cost} {self.currency}"

    def show_saved_data(self):
        outstr = f"Saved Data: {self.name=}, {self.currency=}, {self._used_currency=} {self.price=}, {self.shipping_cost=}"
        print(outstr)
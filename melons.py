"""This file should have our order classes in it."""
from random import randint
from datetime import datetime

class AbstractMelonOrder(object):

    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax
        try:
            self.qty < 100
        except TooManyMelonsError:
            print "TOO MANY MELONS!!!"


    def get_base_price(self):
        """Create random base price"""

        base_price = randint(5, 9)

        current_date_and_time = datetime.timetuple(datetime.now())
        current_hour = current_date_and_time[3]
        current_day = current_date_and_time[6]

        if current_day in [0, 1, 2, 3, 4] and current_hour in [8, 9, 10, 11]:
            base_price += 4
        
        return base_price


    def get_total(self):
        """Calculate price."""

        base_price = self.get_base_price()
        
        if self.species == "Christmas":
            base_price *= 1.5
        
        total = (1 + self.tax) * self.qty * base_price
        
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        super(DomesticMelonOrder, self).__init__(species, qty, "domestic", 0.08)
       

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""

        super(InternationalMelonOrder, self).__init__(species, qty, "international", 0.17)
        self.country_code = country_code
        
    
    def get_total(self):
        """Calculate price."""

        total = super(InternationalMelonOrder, self).get_total()
        if self.qty < 10:
            total += 3
        return total
    

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    """A US government melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        super(GovernmentMelonOrder, self).__init__(species, qty, "domestic", 0)
        self.passed_inspection = False

    def mark_inspection(self, passed):
        """Check inspection."""
        if passed == True:
            self.passed_inspection = True


class TooManyMelonsError(ValueError):
    """An exception that is raised when an order is more than 100 melons."""
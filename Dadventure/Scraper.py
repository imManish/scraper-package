from Dadventure.Resources.Driver import Driver as client_class

# Instance create method
def createInstance():
    return True

__author__ = "Dadventures"

# This is official Scraper class which creates client of request
# @return object of other class.
class Scraper:
    # Construct the apikey and domain
    def __new__(cls, terms, **kwargs):
        if not createInstance():
            raise(RuntimeError, "Count not create instance")
        # Super instance call with reutrn object
        instance = super(Scraper, cls).__new__(cls)
        instance.validate(terms)
        instance.terms = terms
        return client_class(instance.terms)

    def __init__(self) -> object:
        # This init method should return none
        pass

    # Validate credentials
    def validate(self, terms):
        try:
            if not terms:
                raise ("Missing terms")
        except ValueError:
            pass
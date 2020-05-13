from .CurrencyRequest import CurrencyRequest
from .CurrencyDisplay import CurrencyDisplay
from .CurrencyAbbreviationData import CurrencyAbbreviationData
import sys

class CurrencyInteraction():

    def __init__(self, currency_validator):
        self.currency_abbreviation_data = CurrencyAbbreviationData()
        self.currency_validator = currency_validator


    def start_interaction(self,currency_validator):
        """
        Processes two command line arguments: amount and currency_code_root.
        Prints out all related currencies.
        """
        amount = currency_validator.amount
        currency_root = currency_validator.currency_code_root
        currency_target = currency_validator.currency_code_target
        currency_request = CurrencyRequest(amount, currency_root, currency_target)
        currency_answer = currency_request.fetch_currency_convertion()
        currency_display = CurrencyDisplay(currency_answer)
        currency_display.print_currency_answer()

    def get_target_currency_from_user(self):
        valid_currency_code = False
        while(not valid_currency_code):
            currency_code = input("Please provide the target-currency code.\n"
                                    "If you would like to see all currency codes, press A\n").upper().strip()
            if currency_code.__eq__("A"):
                self.currency_abbreviation_data.print_currency_abbreviations()

            if self.is_currency_code_valid(currency_code) == False:
                print("Not a valid Currency abbreviation, try again.")
                print()
            else:
                valid_currency_code = True

        return currency_code

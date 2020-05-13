from .CurrencyAbbreviationData import CurrencyAbbreviationData

class CurrencyValidator():

    #2 command line arguments: amount and currency_target
    def __init__(self, amount, currency_code_root, currency_code_target):
        self.currency_abbreviation_data = CurrencyAbbreviationData()
        self.amount = self.format_amount(amount)
        self.currency_code_root = self.evaluate_currency_code(currency_code_root)
        self.currency_code_target = currency_code_target
        if not self.currency_code_target == 42:
            if self.evaluate_currency_code(self.currency_code_target) == -2:
                exit()
        #Error - cases -1 / -2
        if self.amount == -1 or self.currency_code_root == -2:
            exit(-1)

    def format_amount(self, amount):
        try:
            amount = float(amount.replace(",", "."))
            amount = round(amount, 2)
            return amount
        except:
            print("ERROR -1: No valid amount - format was given. Call the help parameter for instructions how to use the Currency_Exchanger.")
            return -1

    def evaluate_currency_code(self ,currency_code):
        for dictionary_code in self.currency_abbreviation_data.complete_dictionary.values():
            if currency_code == dictionary_code[0]:
                return currency_code

        print("ERROR -2: Invalid Currency - Code was given. Call the help parameter for instructions how to use the Currency_Exchanger.")
        return -2

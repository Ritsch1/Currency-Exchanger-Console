from prettytable import PrettyTable

class CurrencyAbbreviationData():

    def __init__(self):
        """
        The currency abbreviations - dictionaries contain a Currency name (KEY)
        and map it to a tupel of (currency-abbreviation,currency-symbol)
        """
        self.european_currency_abbreviations = {
            "Swiss Franc":("CHF","Fr."),
            "Euro":("EUR","€"),
            "Pound":("GBP","£"),
            "Swedish Krona":("SEK","kr"),
            "Danish Krona":("DKK","kr"),
            "Krona Norwegia":("NOK","kr"),
            "Czech Koruna":("CZK","Kč"),
            "Zloty (POLAND)":("PLN","zł"),
            "Croatian Kuna":("HRK","kn"),
            "Bulgarian Lev":("BGN","лв"),
            "Hungarian Forint":("HUF","ft"),
            "Ukrainian hryvna":("UAH","₴"),
            "Romanian Leu":("RON","lei"),
            "Ruble (RUSSIA)": ("RUB", "₽"),
            "Turkish Lira": ("TRY", "₺")
        }

        self.african_middleEast_currency_abbreviations = {

            "Israeli Shekel": ("ILS","₪"),
            "Rand (SOUTH-AFRICA)": ("ZAR", "R"),
        }

        self.american_currency_abbreviations = {
            "Dollar": ("USD", "$"),
            "Canadian Dollar": ("CAD", "C$"),
            "Mexican Peso": ("MXN", "Mex$"),
            "Brazilian Real": ("BRL","R$"),
        }

        self.asian_pacificRegion_currency_abbreviations = {
            "Australian Dollar": ("AUD", "A$"),
            "Japanese Yen": ("JPY", "¥"),
            "Yuan (CHINA)": ("CNY", "CN¥"),
            "Indonesian rupiah": ("IDR","RP"),
            "Indian Rupee": ("INR", "₹"),
            "Malaysian Ringgit" :("MYR","RM"),
            "New Zealand Dollar": ("NZD", "NZ$"),
            "Singapore Dollar": ("SGD", "S$"),
            "South Korean Won": ("KRW","₩"),
            "Thai baht": ("THB","฿"),
            "Hong Kong Dollar": ("HKD", "HK$"),
        }
        self.complete_dictionary = {}
        for dictionary in (self.african_middleEast_currency_abbreviations,
                           self.american_currency_abbreviations,
                           self.asian_pacificRegion_currency_abbreviations,
                           self.european_currency_abbreviations):
            self.complete_dictionary.update(dictionary)

    def print_currency_abbreviations(self):
        european_table = PrettyTable(["Currency","Currency Code"])
        for currency, currency_code in self.european_currency_abbreviations.items():
            european_table.add_row([currency,currency_code[0]])
        print("European Currencies")
        print(european_table)

        african_middle_East_table = PrettyTable(["Currency","Currency Code"])
        for currency, currency_code in self.african_middleEast_currency_abbreviations.items():
            african_middle_East_table.add_row([currency, currency_code[0]])
        print("African/Middle-East Currencies")
        print(african_middle_East_table)

        american_table = PrettyTable(["Currency", "Currency Code"])
        for currency, currency_code in self.american_currency_abbreviations.items():
            american_table.add_row([currency, currency_code[0]])
        print("American Currencies")
        print(american_table)

        asian_table = PrettyTable(["Currency", "Currency Code"])
        for currency, currency_code in self.asian_pacificRegion_currency_abbreviations.items():
            asian_table.add_row([currency, currency_code[0]])
        print("Asian Currencies")
        print(asian_table)

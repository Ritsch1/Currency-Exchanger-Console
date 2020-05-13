import sys
from CurrencyClasses.CurrencyAbbreviationData import CurrencyAbbreviationData
from CurrencyClasses.CurrencyInteraction import CurrencyInteraction
from CurrencyClasses.CurrencyValidator import CurrencyValidator


if len(sys.argv) == 2 and sys.argv[1].lower()=="currencies":
    currency_abbreviations = CurrencyAbbreviationData()
    currency_abbreviations.print_currency_abbreviations()

if len(sys.argv) == 2 and sys.argv[1].lower()=="help" or sys.argv[1].lower()=="-h":
    print("If you want to look up all available currencies and their currency-codes give the parameter <currencies>\n\n")
    print("The Currency_Exchanger accepts the following parameter combinations:\n\n")
    print("python Currency_Exchanger <amount> <root_currency_code>")
    print("-> This will give you all exchange amount and rates available for the root currency provided\n\n")
    print("python Currency_Exchanger <amount> <root_currency_code> <target_currency_code>")
    print("-> This will give you only the exchange rate and amount between the exact two currencies provided\n\n")
    print("Description of parameters:")
    print("amount -> The amount you want to exchange as a positive number.")
    print("root_currency_code -> The 3-char ISO 4217 currency code of the currency you want to exchange from")
    print("target_currency_code -> The 3-char ISO 4217 currency code of the currency you want to exchange to\n\n")
    print("Sample Calls:")
    print("-> python Currency_Exchanger 200 USD")
    print("This will give you all exchange amounts and rates for the amount of 200 Dollar with USD as the root currency.")
    print("python Currency_Exchanger 200 USD EUR")
    print("-> This will give you the exchange amount and rate for 200 Dollars in Euro.")

if len(sys.argv) == 3:
    currency_validator = CurrencyValidator(sys.argv[1], sys.argv[2],42)
    currency_interaction = CurrencyInteraction(currency_validator)
    currency_interaction.start_interaction(currency_validator)

elif len(sys.argv) == 4:
    currency_validator = CurrencyValidator(sys.argv[1], sys.argv[2], sys.argv[3])
    currency_interaction = CurrencyInteraction(currency_validator)
    currency_interaction.start_interaction(currency_validator)
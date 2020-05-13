from prettytable import PrettyTable

class CurrencyDisplay():
    def __init__(self, currency_answer):
        self.currency_answer = currency_answer

    def print_currency_answer(self):
        table = PrettyTable(["Amount", "Currency Root", "Currency Target", "Amount Target", "Exchange Rate"])
        for i in range(len(self.currency_answer.currency_targets)):
            table.add_row([str(self.currency_answer.amount_root) + " " +self.currency_answer.currency_root,
                          self.currency_answer.currency_root,
                          self.currency_answer.currency_targets[i],
                          str(self.currency_answer.amount_targets[i])+" "+self.currency_answer.currency_targets[i],
                          self.currency_answer.exchange_rates[i]])
        print(table)
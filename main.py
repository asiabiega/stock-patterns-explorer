import apriori
import data_handlers

def print_rules(rules):
    for rule in rules:
        print rule['rule']
        print "\tsupp: %f" % rule['support']
        print "\tconf: %f" % rule['confidence']
        print "\tlift: %f" % rule['lift']
        print "\tconv: %f" % rule['conviction']
        print "\tlevg: %f" % rule['leverage']

if __name__ == '__main__':

    test_transactions = [
        [1,2,3,4,5],
        [1,3],
        [1,2,3,4],
        [4,5],
        [3,4,5],
        [1],
        [1,2],
        [1,2,3,4],
        [1,3,5],
        [1,2,4]
    ]

    stock_transactions = (data_handlers.CSVDataHandler(transaction_len=10)
                            .handle_data('data/google.csv_kwantylowo.csv'))

    rule_explorer = apriori.AprioriRuleExplorer(transaction_set=stock_transactions, 
                                                min_support=0.09)

    rules = rule_explorer.run()

    print_rules(sorted(rules, key=lambda x: x['leverage'], reverse=True))

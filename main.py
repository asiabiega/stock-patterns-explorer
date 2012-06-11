import apriori
import data_handlers
import argparse

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


    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--file', type=str)
    parser.add_argument('--supp', type=float, default=0.09, nargs='?')
    parser.add_argument('--trans_len', type=int, default=10, nargs='?')

    args = parser.parse_args()

    stock_transactions = (data_handlers.CSVDataHandler(transaction_len=args.trans_len)
                            .handle_data(args.file))

    rule_explorer = apriori.AprioriRuleExplorer(transaction_set=stock_transactions, 
                                                min_support=args.supp)

    rules = rule_explorer.run()

    print_rules(sorted(rules, key=lambda x: x['leverage'], reverse=True))

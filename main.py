import apriori
import data_handlers

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
                                                min_support=0.05)

    rules = rule_explorer.run()

    print rules

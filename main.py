import apriori

if __name__ == '__main__':

    transactions = [
        [1,2,3,4,5],
        [1,3],
        [1,3,5],
        [4,5],
        [3,4,5],
        [1],
        [1,2],
        [1,2,3],
        [1,3,5],
        [1,2,4]
    ]

    rule_explorer = apriori.AprioriRuleExplorer(transaction_set=transactions, 
                                                min_support=0.25)

    rules = rule_explorer.run()

    print rules

import csv
import itertools

class CSVDataHandler(object):

    def __init__(self, transaction_len):
        self.transaction_len = transaction_len

    def handle_data(self, filename):
        with open(filename, 'r') as f:
            reader = csv.reader(f, delimiter=",")
            raw_data = [row[1] for row in reader]
            
            transactions = []
            for i in xrange(len(raw_data) - self.transaction_len + 1):
                transactions.append(raw_data[i:i+self.transaction_len])

            return transactions

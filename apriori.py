import itertools

class AprioriRuleExplorer(object):

    def __init__(self, transaction_set, min_support):
        super(AprioriRuleExplorer, self).__init__()
        self.transaction_set = transaction_set
        self.min_support = min_support

        self.rules = []

    def run(self):
        size = 1
        frequent = self.filter_candidates([[s]
                        for s in set(itertools.chain(*self.transaction_set))])

        while frequent:
            size += 1
            candidates = list(self.get_candidates(size=size, frequent=frequent))
            frequent = self.filter_candidates(candidates)

            self.rules.extend(frequent)

        rules = set(self.rules)
        return [{'rule': rule, 
                 'support': self.support(rule),
                 'confidence': self.confidence(rule),
                 'lift': self.lift(rule),
                 'leverage': self.leverage(rule),
                 'conviction': self.conviction(rule)} for rule in rules]

    def get_candidates(self, size, frequent):
        singletons = set(itertools.chain(*frequent))
        return itertools.permutations(singletons, size)

    def filter_candidates(self, candidates):
        return [s for s in candidates if self.support(s) > self.min_support]

    def is_subsequence(self, seq1, seq2):
        for i in xrange(len(seq2) - len(seq1) + 1):
            success = True
            for j in xrange(len(seq1)):
                if seq1[j] != seq2[i+j]:
                    success = False
                    break
            if success:
                return True
        return False

    def support(self, seq):
        present_in = (lambda s : 
                        sum([self.is_subsequence(s, trans) 
                             for trans in self.transaction_set]))

        return float(present_in(seq)) / len(self.transaction_set)

    def confidence(self, seq):
        lhs, rhs = seq[:-1], seq[-1:]
        return self.support(seq) / self.support(lhs)

    def lift(self, seq):
        lhs, rhs = seq[:-1], seq[-1:]
        return self.support(seq) / (self.support(lhs) * self.support(rhs))

    def leverage(self, seq):
        lhs, rhs = seq[:-1], seq[-1:]
        return self.support(seq) - self.support(lhs) * self.support(rhs)

    def conviction(self, seq):
        lhs, rhs = seq[:-1], seq[-1:]
        return (1 - self.support(rhs)) / (1 - self.confidence(seq))

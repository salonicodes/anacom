class Probability:
    def __init__(val):
        self.prob=val
    def checkforLimit(self):
        if (self.val>=0) and (self.val<=1):
            return True
        return False
    def mutuallyExclusive(p1,p2):
        return Probability(p1.val1+p2.val2)
    def complementryProbability(p1):
        return Probability(1-p1.val)
    def notMutuallyExclusive(p1,p2,p3):
        return Probability(p1.val+p2.val-p3.val)
    def partitionExclusion(l):
        if sum(l)==1:
            return True
        return False
    def condtionalProbability(pAIntersectionB,pA):
        return Probability(pAIntersectionB.val/pA.val)

class Card():
    def __init__(self, suite, rank):
        
        acceptedRanks = ["A","K","Q","J","10","9","8","7","6","5","4","3","2"]
        acceptedSuits = ["HEARTS", "DIAMONDS", "SPADES", "CLUBS"]

        if not isinstance(suite, str):
            raise TypeError(f"Suite expected to be a string, got {type(suite)}")

        if not isinstance(rank, str):
            raise TypeError(f"Rank expected to be a string, got {type(rank)}")

        suiteUpper = suite.upper()
        rankUpper = rank.upper()
        if rankUpper in acceptedRanks:
            pass
        else:
            raise TypeError(f"Added a rank not in rank list {acceptedRanks}, got {rank}")

        if suiteUpper in acceptedSuits:
            pass
        else:
            raise TypeError(f"Added a suite not in suit list {acceptedSuits}, got {suite}")
        
        self.suite = suiteUpper
        self.rank = rankUpper

    def printCard(self):
            print("Rank",self.rank)
            print("Suite",self.suite)

print(__name__)

if __name__ == "__main__":
           card1 = Card(suite="DIAMONDS", rank="A")
           card1.printCard()

           Card2 = Card(suite="Clubs", rank="3")
           Card2.printCard()
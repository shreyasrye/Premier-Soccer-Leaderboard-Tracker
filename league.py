import random
import string


class Team:
    sport = ""
    score, next = None, None

    def __init__(self, score, sport, next=None):
        self.score = score
        self.sport = sport
        if next != None:
            self.next = next

    def calculate_score():
        return # for now (later will be some failsafe algorithm)


class League:

    identifier = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(32))
    head = None
    length = 0

    def __init__(self, leading_team: Team, len):
        self.head = leading_team
        self.length = len





def main():
    l = League()

if __name__ == "__main__":
    main()

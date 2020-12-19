import random
import string


class team:
    score = None

class league:

    identifier = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(32))

    # create team objects here




def main():
    l = league()

if __name__ == "__main__":
    main()

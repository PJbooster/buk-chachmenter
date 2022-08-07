
from lib.st.st import St


class App:

    def run(self):

        broker = St()
        broker.pull_bets()

        pass
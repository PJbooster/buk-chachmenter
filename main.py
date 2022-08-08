#!/usr/bin/env python


"""
plugins for each broker:
st - STS
ef - Fortuna
bc - BetClic
...
"""
from lib.app import App
from lib.st.st import St
from model import (
    db,
    EventOdds,
    League,
    Match,
    EventType,
    Broker,
    Bet,
    Event,
    EventItemType,
    Odds,
)


if __name__ == "__main__":
    application = App()
    # db.create_tables(
    #     [
    #         EventOdds,
    #         League,
    #         Match,
    #         EventType,
    #         Broker,
    #         Bet,
    #         Event,
    #         EventItemType,
    #         Odds,
    #     ]
    # )
    application.run()
    pass

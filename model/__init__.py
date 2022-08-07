from peewee import SqliteDatabase

db = SqliteDatabase("people.db")

from .model import (
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

from peewee import *
from . import db


class League(Model):
    name = TextField()

    class Meta:
        database = db


class Match(Model):
    teamA = TextField()
    teamB = TextField()
    date = DateField()
    league = ForeignKeyField(League, backref="match")

    class Meta:
        database = db  # This model uses the "people.db" database.


class EventType(Model):
    type = TextField()

    class Meta:
        database = db


class Broker(Model):
    broker = TextField()

    class Meta:
        database = db


class Bet(Model):
    match = ForeignKeyField(Match)
    beoker = ForeignKeyField(Broker)

    class Meta:
        database = db


class Event(Model):
    event_type = ForeignKeyField(EventType)
    bet = ForeignKeyField(Bet)

    class Meta:
        database = db


class EventItemType(Model):
    type = TextField()

    class Meta:
        database = db


class Odds(Model):
    event_item_type = ForeignKeyField(EventItemType)
    odds = FloatField()
    odds_time = DateField()

    class Meta:
        database = db


class EventOdds(Model):
    odds = ForeignKeyField(Odds)
    event = ForeignKeyField(Event)

    class Meta:
        database = db

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from flask import url_for
from sqlalchemy import sql
#from guokr.platform.sqlalchemy.types import JSONType

from studio.core.engines import db


__all__ = [
    'MatchPlayerModel',
    'MatchModel',
    'RoundModel',
    'BoardModel',
]


class MatchPlayerModel(db.Model):
    __tablename__ = 'match_player'

    id = db.Column(db.Integer(), nullable=False, primary_key=True)
    match_id = db.Column(db.Integer(), db.ForeignKey('match.id'),
                        nullable=False,
                        index=True)
    team_id = db.Column(db.Integer(), db.ForeignKey('team.id'),
                        nullable=False,
                        index=True)
    score = db.Column(db.Integer(), nullable=False)
    is_home = db.Column(db.Boolean(), nullable=False,
                        server_default=sql.true())
#    info = db.Column(JSONType(), nullable=True)
    date_created = db.Column(db.DateTime(timezone=True),
                             nullable=False, index=True,
                             server_default=db.func.current_timestamp())


class MatchModel(db.Model):
    __tablename__ = 'match'

    id = db.Column(db.Integer(), nullable=False, primary_key=True)
    round_id = db.Column(db.Integer(), db.ForeignKey('round.id'),
                         nullable=False,
                         index=True)
    place = db.Column(db.Unicode(1024), nullable=False)
    introduction = db.Column(db.UnicodeText(), nullable=False)
    result = db.Column(db.Unicode(1024), nullable=False)
    date_started = db.Column(db.DateTime(timezone=True),
                             nullable=True, index=True)
    date_created = db.Column(db.DateTime(timezone=True),
                             nullable=False, index=True,
                             server_default=db.func.current_timestamp())

    players = db.relationship(
        'MatchPlayerModel',
        primaryjoin='MatchModel.id==MatchPlayerModel.match_id',
        order_by=MatchPlayerModel.is_home.desc(),
        foreign_keys='[MatchPlayerModel.match_id]',
        backref=db.backref(
            'match', lazy='subquery', innerjoin=True),
        passive_deletes='all', lazy='dynamic')

    @property
    def url(self):
        return url_for("views.match", cid=self.id)

    def __str__(self):
        return self.name


class RoundModel(db.Model):
    __tablename__ = 'round'

    id = db.Column(db.Integer(), nullable=False, primary_key=True)
    board_id = db.Column(db.Integer(), db.ForeignKey('board.id'),
                         nullable=False,
                         index=True)
    num = db.Column(db.Integer(), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True),
                             nullable=False, index=True,
                             server_default=db.func.current_timestamp())

    matches = db.relationship(
        'MatchModel',
        primaryjoin='RoundModel.id==MatchModel.round_id',
        order_by=MatchModel.date_created.desc(),
        foreign_keys='[MatchModel.round_id]',
        backref=db.backref(
            'round', lazy='subquery', innerjoin=True),
        passive_deletes='all', lazy='dynamic')

    @property
    def url(self):
        return url_for("views.round", cid=self.id)

    def __str__(self):
        return '第%s轮' % str(self.num)


class BoardModel(db.Model):
    __tablename__ = 'board'

    id = db.Column(db.Integer(), nullable=False, primary_key=True)
    name = db.Column(db.Unicode(256), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True),
                             nullable=False, index=True,
                             server_default=db.func.current_timestamp())

    rounds = db.relationship(
        'RoundModel',
        primaryjoin='BoardModel.id==RoundModel.board_id',
        order_by=RoundModel.num.desc(),
        foreign_keys='[RoundModel.board_id]',
        backref=db.backref(
            'board', lazy='subquery', innerjoin=True),
        passive_deletes='all', lazy='dynamic')

    @property
    def url(self):
        return url_for("views.board", cid=self.id)

    def __str__(self):
        return self.name

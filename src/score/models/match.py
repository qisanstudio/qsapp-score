# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from flask import url_for
from studio.core.engines import db
from score.models.team import MatchTeamModel


__all__ = [
    'MatchModel',
    'RoundModel',
    'BoardModel',
]


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

    teams = db.relationship('TeamModel', secondary=MatchTeamModel.__table__)

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

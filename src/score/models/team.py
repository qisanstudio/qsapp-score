# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from flask import url_for
from studio.core.engines import db


__all__ = [
    'TeamModel',
]


class MatchTeamModel(db.Model):
    __tablename__ = 'match_team'

    match_id = db.Column(db.Integer(), db.ForeignKey('match.id'),
                         primary_key=True, index=True)
    team_id = db.Column(db.Integer(),
                       db.ForeignKey('team.id'), primary_key=True, index=True)


class TeamModel(db.Model):
    __tablename__ = 'team'

    id = db.Column(db.Integer(), nullable=False, primary_key=True)
    name = db.Column(db.Unicode(256), nullable=False, unique=True, index=True)
    introduction = db.Column(db.UnicodeText(), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True),
                             nullable=False, index=True,
                             server_default=db.func.current_timestamp())

    @property
    def url(self):
        return url_for("views.team", cid=self.id)

    def __str__(self):
        return self.name

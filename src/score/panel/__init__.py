# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .team import Team
from .match import Match, Round, Board


from flask.ext.admin import Admin


admin = Admin(name='后台管理', url='/admin')


# 人员管理
admin.add_view(Team(name='队伍', category='人员管理', endpoint='team'))


# 比赛管理
admin.add_view(Match(name='比赛', category='比赛管理', endpoint='match'))
admin.add_view(Round(name='论次', category='比赛管理', endpoint='round'))
admin.add_view(Board(name='积分榜', category='比赛管理', endpoint='board'))

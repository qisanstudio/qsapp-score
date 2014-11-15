# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from wtforms import validators
from jinja2 import Markup
from flask.ext.admin.contrib.sqla import ModelView
from studio.core.engines import db

from score.models import MatchModel, RoundModel, BoardModel


class Match(ModelView):

    column_labels = {'id': 'ID',
                     'round': '轮次',
                     'place': '场地',
                     'introduction': '简介',
                     'result': '结果',
                     'date_started': '开始时间',
                     'date_created': '创建时间'}
    column_list = ['id', 'place', 'introduction', 'result',
                   'date_started', 'date_created']
    column_searchable_list = ['place', 'introduction']
    column_default_sort = ('date_created', True)

    def __init__(self, **kwargs):
        super(Match, self).__init__(MatchModel, db.session, **kwargs)

    def create_form(self, obj=None):
        form = super(Match, self).create_form()
        delattr(form, 'teams')
        delattr(form, 'date_created')
        return form

    def edit_form(self, obj=None):
        form = super(Match, self).edit_form(obj=obj)
        delattr(form, 'teams')
        delattr(form, 'date_created')
        return form


class Round(ModelView):

    column_labels = {'id': 'ID',
                     'num': '轮次',
                     'date_created': '创建时间'}
    column_list = ['id', 'num', 'date_created']
    column_default_sort = ('date_created', True)

    def __init__(self, **kwargs):
        super(Round, self).__init__(RoundModel, db.session, **kwargs)

    def create_form(self, obj=None):
        form = super(Round, self).create_form()
        delattr(form, 'matches')
        delattr(form, 'date_created')
        return form

    def edit_form(self, obj=None):
        form = super(Round, self).edit_form(obj=obj)
        delattr(form, 'matches')
        delattr(form, 'date_created')
        return form


class Board(ModelView):

    column_labels = {'id': 'ID',
                     'name': '名称',
                     'date_created': '创建时间'}
    column_searchable_list = ['name']
    column_list = ['id', 'name', 'date_created']
    column_default_sort = ('date_created', True)

    def __init__(self, **kwargs):
        super(Board, self).__init__(BoardModel, db.session, **kwargs)

    def create_form(self, obj=None):
        form = super(Board, self).create_form()
        delattr(form, 'rounds')
        delattr(form, 'date_created')
        return form

    def edit_form(self, obj=None):
        form = super(Board, self).edit_form(obj=obj)
        delattr(form, 'rounds')
        delattr(form, 'date_created')
        return form

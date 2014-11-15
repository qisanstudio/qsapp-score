# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from wtforms import validators
from jinja2 import Markup
from flask.ext.admin.contrib.sqla import ModelView
from studio.core.engines import db

from score.models import TeamModel


class Team(ModelView):

    column_labels = {'id': 'ID',
                     'name': '队名',
                     'introduction': '简介',
                     'date_created': '创建时间'}
    column_list = ['id', 'name', 'introduction', 'date_created']
    column_searchable_list = ['name', 'introduction']
    column_default_sort = ('date_created', True)

    def __init__(self, **kwargs):
        super(Team, self).__init__(TeamModel, db.session, **kwargs)

    def create_form(self, obj=None):
        form = super(Team, self).create_form()
        delattr(form, 'date_created')
        return form

    def edit_form(self, obj=None):
        form = super(Team, self).edit_form(obj=obj)
        delattr(form, 'date_created')
        return form

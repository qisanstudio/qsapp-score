from studio.core.engines import db
import factory

from score.models import MatchModel, RoundModel, BoardModel, TeamModel



class BaseFactory(factory.SQLAlchemyModelFactory):

    class Meta:
        abstract = False
        sqlalchemy_session = db.session


class MatchFactory(BaseFactory):

    class Meta:
        model = MatchModel
        inline_args = ('place', 'result')
        exclude = ('now', )

    id = factory.Sequence(lambda n: n)
    place = u'克劳沃足球基地'
    introduction = factory.LazyAttribute(lambda o: u'%s-漫园足球联赛' % o.place
    result = u'1:0'
    now = factory.LazyAttribute(lambda o: datetime.datetime.utcnow())
    date_started = factory.LazyAttribute(lambda o: o.now)
    date_created = factory.LazyAttribute(lambda o: o.now)

    teams = factory.SubFactory(TeamFactory)


class RoundFactory(factory.Factory):

    class Meta:
        model = RoundModel


class BoardFactory(factory.Factory):

    class Meta:
        model = BoardModel


class TeamFactory(factory.Factory):

    class Meta:
        model = TeamModel

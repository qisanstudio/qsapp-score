"""create_table

Revision ID: 42f4a0f4afd9
Revises: None
Create Date: 2014-11-15 16:53:22.716676

"""

# revision identifiers, used by Alembic.
revision = '42f4a0f4afd9'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(u'board',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('name', sa.Unicode(256), nullable=False),
        sa.Column('date_created', sa.DateTime(timezone=True),
                                  nullable=False, index=True,
                                  server_default=sa.func.current_timestamp()))

    op.create_table(u'round',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('board_id', sa.Integer(),
                              sa.ForeignKey('board.id'), nullable=True),
        sa.Column('num', sa.Integer(), nullable=False),
        sa.Column('date_created', sa.DateTime(timezone=True),
                                  nullable=False, index=True,
                                  server_default=sa.func.current_timestamp()))

    op.create_table(u'match',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('round_id', sa.Integer(),
                              sa.ForeignKey('round.id'), nullable=True),
        sa.Column('place', sa.Unicode(1024), nullable=False),
        sa.Column('introduction', sa.UnicodeText(), nullable=False),
        sa.Column('result', sa.Unicode(1024), nullable=False),
        sa.Column('date_started', sa.DateTime(timezone=True),
                                  nullable=False, index=True),
        sa.Column('date_created', sa.DateTime(timezone=True),
                                  nullable=False, index=True,
                                  server_default=sa.func.current_timestamp()))

    op.create_table(u'team',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('name', sa.Unicode(256), nullable=False),
        sa.Column('introduction', sa.UnicodeText(), nullable=False),
        sa.Column('date_created', sa.DateTime(timezone=True),
                                  nullable=False, index=True,
                                  server_default=sa.func.current_timestamp()))

    op.create_table(u'match_team',
        sa.Column('match_id', sa.Integer(), sa.ForeignKey('match.id'),
                              primary_key=True, index=True),
        sa.Column('team_id', sa.Integer(), sa.ForeignKey('team.id'),
                              primary_key=True, index=True))


def downgrade():
    op.drop_table(u'match_team')
    op.drop_table(u'team')
    op.drop_table(u'match')
    op.drop_table(u'round')
    op.drop_table(u'board')

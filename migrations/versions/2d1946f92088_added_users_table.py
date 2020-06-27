"""Added users table


Revision ID: 2d1946f92088
Revises: 
Create Date: 2020-06-27 05:31:25.873450

"""
from alembic import op
from sqlalchemy import orm
from migrations import helper

# revision identifiers, used by Alembic.
revision = '2d1946f92088'
down_revision = None
branch_labels = None
depends_on = None

Session = orm.sessionmaker()
g_bind = op.get_bind()


def upgrade():
    helper.execute(bind=g_bind, filename="added_users/upgrade.sql")


def downgrade():
    helper.execute(bind=g_bind, filename="added_users/downgrade.sql")

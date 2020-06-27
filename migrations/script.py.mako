"""${message}


Revision ID: ${up_revision}
Revises: ${down_revision | comma,n}
Create Date: ${create_date}

"""
from alembic import op
from sqlalchemy import orm
from migrations import helper
${imports if imports else ""}

# revision identifiers, used by Alembic.
revision = ${repr(up_revision)}
down_revision = ${repr(down_revision)}
branch_labels = ${repr(branch_labels)}
depends_on = ${repr(depends_on)}

Session = orm.sessionmaker()
g_bind = op.get_bind()

def upgrade():
    helper.execute(bind=g_bind, filename="${message}/upgrade.sql")

def downgrade():
    helper.execute(bind=g_bind, filename="${message}/downgrade.sql")

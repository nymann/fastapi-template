from chessdb_api.models import DB
from sqlalchemy.dialects import postgresql as psql
from sqlalchemy import func


class User(DB.Model):
    __tablename__ = "users"

    identifier = DB.Column(psql.UUID(as_uuid=True), primary_key=True)
    email = DB.Column(DB.String(), unique=True, index=True, nullable=False)
    name = DB.Column(DB.String(), index=True)
    admin = DB.Column(DB.Boolean(), default=False)
    created_at = DB.Column(DB.DateTime(timezone=True),
                           server_default=func.now())
    password = DB.Column(DB.String(), nullable=False)

    def __init__(self, email: str, name: str, admin: bool = False):
        self.email = email
        self.name = name
        self.admin = admin

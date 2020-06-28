from datetime import datetime

from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy_utils import EmailType, generic_repr

from fastapi_template.models import DB

DB.JSONB, DB.UUID, DB.EmailType = (JSONB, UUID, EmailType)


@generic_repr
class Base(DB.Model):
    __abstract__ = True
    created_at = DB.Column(DB.DateTime,
                           default=datetime.utcnow,
                           server_default=DB.func.now())

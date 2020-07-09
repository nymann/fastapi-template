from fastapi_template.core.db import DB


class Model(DB.Model):
    """Model.
    """

    __tablename__ = "users"

    identifier = DB.Column(DB.UUID(as_uuid=False),
                           primary_key=True,
                           server_default=DB.text("uuid_generate_v4()"))
    email = DB.Column(DB.EmailType, unique=True, index=True, nullable=False)
    name = DB.Column(DB.String(), index=True)
    is_admin = DB.Column(DB.Boolean(), default=False)
    password = DB.Column(DB.String(), nullable=False)

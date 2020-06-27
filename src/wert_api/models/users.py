from wert_api.models import DB


class User(DB.Model):
    __tablename__ = "users"

    email = DB.Column(DB.String(), primary_key=True)
    name = DB.Column(DB.String())

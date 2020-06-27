import pathlib

from sqlalchemy import orm


def execute(bind, filename: str):
    session = orm.Session(bind=bind)
    file_path = pathlib.Path(f"migrations/versions/{filename}").absolute()
    with open(file_path) as f:
        sql_to_execute = f.read()
        session.execute(sql_to_execute)
        session.commit()

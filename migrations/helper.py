"""This module is a helper method for making migrations less of a pain."""
import pathlib

from sqlalchemy import orm


def execute(bind, filename: str):
    """Execute the content of an SQL (migrations) file.

    Args:
        bind: Binding to the database
        filename (str): The filename excluding path.
    """
    session = orm.Session(bind=bind)
    str_file_path = "migrations/versions/{filename}".format(filename=filename)
    file_path = pathlib.Path(str_file_path).absolute()

    with open(file_path) as sql_file:
        sql_to_execute = sql_file.read()
        session.execute(sql_to_execute)
        session.commit()

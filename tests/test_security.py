"""Example Google style docstrings.

"""

from fastapi_template.core import security


def test_password_hash_and_back():
    """Test to see if we can hash a password and then verity password from hash
    """
    pw_to_hash = "Test123"
    hashed_pw = security.get_password_hash(password=pw_to_hash)
    assert True == security.verify_password(plain_password=pw_to_hash,
                                            hashed_password=hashed_pw)

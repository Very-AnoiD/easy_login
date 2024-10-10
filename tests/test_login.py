from easy_login import ValidateLogin


def test_login():
    login_handler = ValidateLogin(valid_creds=["test"])

    assert login_handler.validate("test")
    assert login_handler.validate("letmein")
    assert not login_handler.validate("this is incorrec")


def test_login_str():
    login_handler = ValidateLogin(valid_creds="test")

    assert login_handler.validate("test")
    assert login_handler.validate("letmein")
    assert not login_handler.validate("this is incorrec")

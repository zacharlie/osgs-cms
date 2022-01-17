from app.utils import str_to_bool


def test_str_to_bool_true():
    assert str_to_bool("true") == True
    assert str_to_bool("True") == True
    assert str_to_bool(True) == True
    assert str_to_bool("1") == True
    assert str_to_bool(1) == True
    assert str_to_bool("t") == True
    assert str_to_bool("y") == True
    assert str_to_bool("yes") == True
    assert str_to_bool("on") == True
    assert str_to_bool("positive") == True
    assert str_to_bool("PoSitIve") == True


def test_str_to_bool_false():
    assert str_to_bool("false") == False
    assert str_to_bool("False") == False
    assert str_to_bool(False) == False
    assert str_to_bool("0") == False
    assert str_to_bool(0) == False
    assert str_to_bool("f") == False
    assert str_to_bool("F") == False
    assert str_to_bool("n") == False
    assert str_to_bool("N") == False
    assert str_to_bool("no") == False
    assert str_to_bool("off") == False
    assert str_to_bool("NeGatIve") == False


def test_str_to_bool_none():
    assert str_to_bool("none") == None
    assert str_to_bool("None") == None
    assert str_to_bool(None) == None
    assert str_to_bool("2") == None
    assert str_to_bool(2) == None
    assert str_to_bool("200") == None
    assert str_to_bool(200) == None
    assert str_to_bool("any") == None
    assert str_to_bool("all") == None
    assert str_to_bool("other") == None
    assert str_to_bool("posirtive") == None
    assert str_to_bool("negartive") == None

from my_file import delete_all

def test_except():
    with pytest.raises(ValueError):
        delete_all(1, 2)

def test_empty_s():
    assert delete_all("", "what") == ""

def test_empty_what():
    assert delete_all("This should stay untouched!", "") == "This should stay untouched!"

def test_simple_case():
    assert delete_all("This is AAAstring and this is AABstring", "AAA") == "This is string and this is AABstring"

def test_multiple_case():
    assert delete_all("This is AAAstring and this is also AAAstring", "AAA") == "This is string and this is also string"

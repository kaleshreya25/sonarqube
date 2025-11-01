from vuln_demo import weak_password_hash, divide

def test_hash_generates_output():
    assert weak_password_hash("a")  # function returns a string

def test_divide_ok():
    assert divide(4, 2) == 2

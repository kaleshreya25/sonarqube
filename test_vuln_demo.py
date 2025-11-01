from vuln_demo import weak_password_hash, divide
import pytest

def test_hash():
    assert weak_password_hash("a")  # will work, but still flagged as weak

def test_divide():
    assert divide(4, 2) == 2

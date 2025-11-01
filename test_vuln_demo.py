import io
import pickle
import sqlite3
import json
from vuln_demo import (
    weak_password_hash,
    divide,
    insecure_deserialization,
    eval_injection,
    sql_injection,
    overly_broad_except,
    duplicate_logic,
    hardcoded_secret,
)

def test_md5_hash():
    result = weak_password_hash("abc")
    assert isinstance(result, str)
    assert len(result) == 32  # md5 hex length

def test_divide_valid():
    assert divide(10, 2) == 5

def test_eval_injection():
    assert eval_injection("2 + 2") == 4

def test_insecure_deserialization():
    data = pickle.dumps({"name": "test"})
    obj = insecure_deserialization(data)
    assert obj["name"] == "test"

def test_sql_injection(tmp_path):
    db_path = tmp_path / "test.db"
    conn = sqlite3.connect(db_path)
    conn.execute("CREATE TABLE users (name TEXT)")
    conn.execute("INSERT INTO users VALUES ('admin')")
    conn.commit()
    conn.close()

    rows = sql_injection(db_path, "admin")
    assert len(rows) == 1

def test_overly_broad_except(capsys):
    overly_broad_except()
    out, _ = capsys.readouterr()
    assert "Error ignored" in out

def test_duplicate_logic(capsys):
    duplicate_logic(6)
    out, _ = capsys.readouterr()
    assert "High value" in out

def test_hardcoded_secret(capsys):
    hardcoded_secret()
    out, _ = capsys.readouterr()
    assert "API key" in out

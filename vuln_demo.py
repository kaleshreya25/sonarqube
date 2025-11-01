import json
import pickle
import sqlite3
from pathlib import Path

from vuln_demo import (
    weak_password_hash,
    command_injection,
    insecure_deserialization,
    eval_injection,
    sql_injection,
    divide,
    read_json,
    overly_broad_except,
    duplicate_logic,
    hardcoded_secret,
)


def test_md5_hash_len():
    out = weak_password_hash("abc")
    assert isinstance(out, str) and len(out) == 32  # md5 hex length


def test_eval_injection():
    assert eval_injection("2 + 2") == 4


def test_insecure_deserialization_roundtrip():
    data = pickle.dumps({"k": "v"})
    obj = insecure_deserialization(data)
    assert obj["k"] == "v"


def test_sql_injection_select(tmp_path: Path):
    db = tmp_path / "t.db"
    conn = sqlite3.connect(db)
    conn.execute("CREATE TABLE users (name TEXT)")
    conn.execute("INSERT INTO users VALUES ('admin')")
    conn.commit()
    conn.close()

    rows = sql_injection(db, "admin")
    assert len(rows) == 1


def test_divide_ok():
    assert divide(10, 2) == 5


def test_read_json(tmp_path: Path):
    p = tmp_path / "cfg.json"
    p.write_text(json.dumps({"a": 1}))
    data = read_json(str(p))
    assert data["a"] == 1


def test_overly_broad_except(capsys):
    overly_broad_except()
    out, _ = capsys.readouterr()
    assert "Error ignored" in out


def test_duplicate_logic(capsys):
    duplicate_logic(9)
    out, _ = capsys.readouterr()
    # at least one line printed
    assert "High value" in out


def test_command_injection_smoke():
    # just ensure it runs; we don't assert the shell output
    command_injection("hello-world")
    assert True


def test_hardcoded_secret_prints(capsys):
    hardcoded_secret()
    out, _ = capsys.readouterr()
    assert "API key" in out

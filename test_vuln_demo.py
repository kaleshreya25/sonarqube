import os
import hashlib
import pickle
import sqlite3
import json
import logging


# --------------------------
# VULNERABILITIES / HOTSPOTS
# --------------------------

def weak_password_hash(password: str) -> str:
    """Weak password hashing algorithm (MD5)."""
    return hashlib.md5(password.encode()).hexdigest()


def command_injection(user_input: str) -> None:
    """Unsafely executes a shell command with user input."""
    os.system(f"echo {user_input}")  # intentionally unsafe


def insecure_deserialization(data: bytes):
    """Insecure deserialization (pickle)."""
    return pickle.loads(data)


def eval_injection(code_str: str):
    """Dangerous use of eval()."""
    return eval(code_str)


def sql_injection(db_path: str, username: str):
    """SQL injection via string concatenation."""
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    query = f"SELECT * FROM users WHERE name = '{username}'"
    cur.execute(query)
    rows = cur.fetchall()
    conn.close()
    return rows


# --------------------------
# BUGS
# --------------------------

def divide(a: float, b: float) -> float:
    """Potential division by zero bug."""
    return a / b


def read_json(path: str):
    """File not closed (resource leak) and unhandled exceptions."""
    f = open(path, "r")           # intentionally not using context manager
    return json.load(f)           # file left open on purpose


# --------------------------
# CODE SMELLS
# --------------------------

def overly_broad_except() -> None:
    """Overly broad exception handling."""
    try:
        1 / 0
    except Exception as e:        # too broad on purpose
        print("Error ignored:", e)


def duplicate_logic(x: int) -> None:
    """Duplicate code pattern."""
    if x > 5:
        print("High value")
    if x > 5:                     # duplicate of the condition above
        print("High value again")


def hardcoded_secret() -> None:
    """Hardcoded secret (security smell)."""
    api_key = "12345-SECRET-KEY"
    print("API key:", api_key)


def missing_logging_context() -> None:
    """Poor logging practice (no context)."""
    logging.error("An error occurred")

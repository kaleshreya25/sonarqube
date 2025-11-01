import os
import hashlib
import pickle
import sqlite3
import json


# ------------------------------
# VULNERABILITIES
# ------------------------------

def weak_password_hash(password):
    """❌ Uses MD5 instead of SHA256 or bcrypt"""
    return hashlib.md5(password.encode()).hexdigest()


def command_injection(user_input):
    """❌ Unsafely executes shell command with user input"""
    os.system(f"echo {user_input}")


def insecure_deserialization(data):
    """❌ Insecure deserialization (can execute arbitrary code)"""
    return pickle.loads(data)


def eval_injection(code):
    """❌ Dangerous use of eval()"""
    return eval(code)


def sql_injection(db_path, username):
    """❌ SQL injection by concatenating user input"""
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    query = f"SELECT * FROM users WHERE name = '{username}'"
    cur.execute(query)
    rows = cur.fetchall()
    conn.close()
    return rows


# ------------------------------
# BUGS
# ------------------------------

def divide(a, b):
    """❌ Division by zero risk"""
    return a / b


def read_json_file(path):
    """❌ Potential unhandled exception if file missing or invalid JSON"""
    f = open(path, "r")  # ❌ File not closed
    return json.load(f)


# ------------------------------
# CODE SMELLS
# ------------------------------

def overly_broad_except():
    """⚠️ Catches all exceptions (too broad)"""
    try:
        risky = 10 / 0
    except Exception as e:  # too broad
        print("Error ignored:", e)


def duplicate_logic(x):
    """⚠️ Duplicate code smell"""
    if x > 10:
        print("High value")
    if x > 10:  # duplicate condition
        print("High value again")


def hardcoded_secret():
    """⚠️ Hardcoded credentials"""
    password = "admin123"  # hardcoded secret
    print("Using password:", password)


if __name__ == "__main__":
    weak_password_hash("test")
    command_injection("hello; rm -rf /")  # intentionally unsafe
    try:
        divide(5, 0)
    except:
        pass
    overly_broad_except()
    duplicate_logic(20)
    hardcoded_secret()

import os
import hashlib
import pickle
import sqlite3
from flask import Flask, request  # unused import (code smell)

# --- VULNERABILITIES ---

def run_command(user_input):
    # Command injection: untrusted input passed to shell
    os.system("echo " + user_input)

def weak_password_hash(pw):
    # Weak hash: MD5 is insecure
    return hashlib.md5(pw.encode()).hexdigest()

def insecure_deserialize(blob):
    # Insecure deserialization (executes code in blob)
    return pickle.loads(blob)

def sql_injection(db_path, username):
    # SQL injection via string concatenation
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    query = "SELECT * FROM users WHERE name = '" + username + "'"  # unsafe
    cur.execute(query)
    rows = cur.fetchall()
    con.close()
    return rows

def eval_user(code_str):
    # Code execution vulnerability
    return eval(code_str)

# --- BUGS / CODE SMELLS ---

def divide(a, b):
    # Bug risk: division by zero not handled
    return a / b

def open_file_leak():
    # Resource leak: file never closed
    f = open("tmp.txt", "w")
    f.write("hello")

def overly_broad_except():
    try:
        risky = 1 / 0
    except Exception as e:  # too broad
        print("swallowed:", e)

def duplicate_block():
    for _ in range(2):
        print("dup")
    for _ in range(2):
        print("dup")  # duplicate

if __name__ == "__main__":
    # simulate usage that will be flagged
    run_command(request.args.get("q") if False else "hi")  # Flask import unused
    weak_password_hash("mypassword")
    insecure_deserialize(pickle.dumps({"a": 1}))  # still flagged as pattern
    sql_injection(":memory:", "bob' OR '1'='1")
    eval_user("__import__('os').system('echo pwned')")
    divide(1, 0)
    open_file_leak()
    overly_broad_except()
    duplicate_block()

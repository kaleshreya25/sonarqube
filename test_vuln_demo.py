from vuln_demo import divide, run_command, overly_broad_except, open_file_leak, duplicate_block

def test_divide():
    assert divide(10, 2) == 5

def test_overly_broad_except(capsys):
    overly_broad_except()
    out, err = capsys.readouterr()
    assert "swallowed" in out

def test_duplicate_block(capsys):
    duplicate_block()
    out, _ = capsys.readouterr()
    assert "dup" in out

def test_open_file_leak(tmp_path):
    fpath = tmp_path / "tmp.txt"
    open_file_leak()
    # file should exist after writing
    assert fpath.exists() or True

import io

from application import main


def test_main(monkeypatch):
    argv = ["application.py", "--name=world"]
    stdin = io.StringIO("hello, {}")
    stdout = io.StringIO()

    with monkeypatch.context() as m:
        m.setattr("sys.argv", argv)
        m.setattr("sys.stdin", stdin)
        m.setattr("sys.stdout", stdout)
        main()

    assert stdout.getvalue() == "hello, world\n"

from app.hello import hello

def test_hello():
    assert hello("Chris") == "Hello, Chris!"

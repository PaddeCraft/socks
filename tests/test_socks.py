from socks.classes import Request


def test_request_object_form():
    r = Request(
        """\
GET /?name=me HTTP/1.1
Host: localhost:8080
Content-Type: application/x-www-form-urlencoded
Content-Length: 16

name=John&age=25""",
        ("localhost", 8080),
    )
    assert r.method == "GET"
    assert r.path == "/"
    assert r.protocol == "HTTP/1.1"
    assert r.headers.get("Host") == "localhost:8080"
    assert r.headers.get("Content-Type") == "application/x-www-form-urlencoded"
    assert r.headers.get("Content-Length") == "16"
    assert r.form.get("name") == "John"
    assert r.form.get("age") == "25"
    assert r.params == {"name": "me"}
    assert r.params.get("name") == "me"
    assert r.params.get("age") == None


def test_request_object_json():
    r = Request(
        """\
GET /?name=me HTTP/1.1
Host: localhost:8080
Content-Type: application/json
Content-Length: 16

{"name": "John", "age": 25}""",
        ("localhost", 8080),
    )
    assert r.method == "GET"
    assert r.path == "/"
    assert r.protocol == "HTTP/1.1"
    assert r.headers.get("Host") == "localhost:8080"
    assert r.headers.get("Content-Type") == "application/json"
    assert r.headers.get("Content-Length") == "16"
    assert r.json.get("name") == "John"
    assert r.json.get("age") == 25
    assert r.params == {"name": "me"}
    assert r.params.get("name") == "me"
    assert r.params.get("age") == None

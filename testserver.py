from socks import Socks, Response, ErrorResponse, renderTemplate

from socks.constants import *

app = Socks()
app2 = Socks(prefix="/app2")
app3 = Socks(prefix="/app3")

app2.registerSubapp(app3)
app.registerSubapp(app2)


@app.route("/", methods=["GET", "POST"])
def index(req):
    return Response(
        "<h1>"
        + req.method
        + "</h1>"
        + (("<p>BODY: " + req.body) if not req.method == "GET" else ""),
        contentType="text/html",
    )


@app.route("/test_error_code")
def test_error_code(req):
    res = renderTemplate(
        "test.html",
        code=req.params.get("code"),
        desc=ERROR_CODES[str(req.params.get("code"))],
    )
    return res


@app.route("/error_resp")
def error_resp(req):
    return ErrorResponse(403)


@app2.route("/")
def test_app_2(req):
    return "Test2"


@app3.route("/")
def test_app_2(req):
    return "Test3"


if __name__ == "__main__":
    app.run(reload=True, host="0.0.0.0")

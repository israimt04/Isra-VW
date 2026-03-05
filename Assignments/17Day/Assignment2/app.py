from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    # If form submitted
    if request.method == "POST":
        name = request.form.get("name")

        response = make_response(render_template("index.html", name=name, count=1))
        response.set_cookie("username", name)
        response.set_cookie("count", "1")

        return response

    # If cookie exists
    name = request.cookies.get("username")
    count = request.cookies.get("count")

    if name and count:
        count = int(count) + 1
        response = make_response(render_template("index.html", name=name, count=count))
        response.set_cookie("count", str(count))
        return response

    # First visit → show form only
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
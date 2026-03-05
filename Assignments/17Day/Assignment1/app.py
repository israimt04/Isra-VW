from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def register():
    error = ""
    success = ""

    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        # Validation
        if not name or not email or not password:
            error = "Fields should not be blank"
        elif "@" not in email:
            error = "Email should contain @ symbol"
        elif len(password) < 5 or len(password) > 8:
            error = "Password must be between 5 and 8 characters"
        else:
            success = "Registration Successful!"

    return render_template("register.html", error=error, success=success)

if __name__ == "__main__":
    app.run(debug=True)

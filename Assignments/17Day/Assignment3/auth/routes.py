from flask import render_template, request, redirect, make_response, url_for
from auth import auth_bp

@auth_bp.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        username = request.form.get("username")
        role = request.form.get("role")
        remember = request.form.get("remember")

        response = make_response(redirect(f"/{role}/dashboard"))

        # Remember Me checked
        if remember:
            max_age = 7 * 24 * 60 * 60
            response.set_cookie("username", username, max_age=max_age)
            response.set_cookie("user_role", role, max_age=max_age)
        else:
            # Session cookie
            response.set_cookie("username", username)
            response.set_cookie("user_role", role)

        return response

    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    response = make_response(redirect(url_for("auth.login")))
    response.delete_cookie("username")
    response.delete_cookie("user_role")
    return response
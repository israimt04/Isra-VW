from flask import render_template, request, redirect
from hr import hr_bp

@hr_bp.route("/dashboard")
def dashboard():
    role = request.cookies.get("user_role")

    if role != "hr":
        return redirect("/")

    username = request.cookies.get("username")
    return render_template("hr_dashboard.html", username=username)
from flask import render_template, request, redirect
from employee import employee_bp

@employee_bp.route("/dashboard")
def dashboard():
    role = request.cookies.get("user_role")

    if role != "employee":
        return redirect("/")

    username = request.cookies.get("username")
    return render_template("employee_dashboard.html", username=username)
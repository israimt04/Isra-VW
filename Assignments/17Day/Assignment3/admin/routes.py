from flask import render_template, request, redirect
from admin import admin_bp

@admin_bp.route("/dashboard")
def dashboard():
    role = request.cookies.get("user_role")

    if role != "admin":
        return redirect("/")

    username = request.cookies.get("username")
    return render_template("admin_dashboard.html", username=username)
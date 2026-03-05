from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy employee data
employees = [
    {"id": 1, "name": "Alice", "department": "IT", "salary": 80000},
    {"id": 2, "name": "Bob", "department": "HR", "salary": 60000},
    {"id": 3, "name": "Charlie", "department": "Finance", "salary": 75000},
]

@app.route("/dashboard")
def dashboard():
    role = request.args.get("role", "employee").lower()

    # Define permissions
    permissions = {
        "admin": {
            "can_view_salary": True,
            "can_delete": True,
            "nav_links": ["Home", "Manage Users", "Reports"],
            "title": "Admin Dashboard"
        },
        "manager": {
            "can_view_salary": True,
            "can_delete": False,
            "nav_links": ["Home", "Team Overview"],
            "title": "Manager Dashboard"
        },
        "employee": {
            "can_view_salary": False,
            "can_delete": False,
            "nav_links": ["Home", "My Profile"],
            "title": "Employee Dashboard"
        }
    }

    # Fallback to employee if invalid role
    if role not in permissions:
        role = "employee"

    return render_template(
        "dashboard.html",
        employees=employees,
        role=role,
        permissions=permissions[role]
    )

if __name__ == "__main__":
    app.run(debug=True)
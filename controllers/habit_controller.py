from flask import Blueprint, render_template
from flask_login import login_required

habit_bp = Blueprint("habit", __name__, url_prefix="/habit")


@habit_bp.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")

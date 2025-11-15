from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from models.models import Habit

habit_bp = Blueprint('habits', __name__, url_prefix='/habits')

@habit_bp.route('/dashboard')
@login_required
def dashboard():
    habits = Habit.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', habits=habits)

@habit_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        frequency = request.form['frequency']
        new_habit = Habit(name=name, description=description, frequency=frequency, user_id=current_user.id)
        db.session.add(new_habit)
        db.session.commit()
        flash('Hábito agregado correctamente', 'success')
        return redirect(url_for('habits.dashboard'))
    return render_template('habits/create.html')

@habit_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    habit = Habit.query.get_or_404(id)
    if request.method == 'POST':
        habit.name = request.form['name']
        habit.description = request.form['description']
        habit.frequency = request.form['frequency']
        db.session.commit()
        flash('Hábito actualizado', 'info')
        return redirect(url_for('habits.dashboard'))
    return render_template('habits/edit.html', habit=habit)

@habit_bp.route('/delete/<int:id>')
@login_required
def delete(id):
    habit = Habit.query.get_or_404(id)
    db.session.delete(habit)
    db.session.commit()
    flash('Hábito eliminado', 'danger')
    return redirect(url_for('habits.dashboard'))

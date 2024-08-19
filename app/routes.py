from flask import Blueprint, render_template, request, redirect, url_for
from flask import current_app  # Add this import
from app import db
from app.models import Message

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message_content = request.form['content']
        new_message = Message(content=message_content)
        db.session.add(new_message)
        db.session.commit()
        return redirect(url_for('main.index'))  # Change 'bp.index' to 'main.index'

    messages = Message.query.all()
    return render_template('index.html', messages=messages)
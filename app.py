from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the Message model
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message_content = request.form['content']
        new_message = Message(content=message_content)
        db.session.add(new_message)
        db.session.commit()
        return redirect(url_for('index'))

    messages = Message.query.all()
    return render_template('templates/index.html', messages=messages)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', debug=True)
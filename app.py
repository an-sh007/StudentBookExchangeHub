from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DATABASE = 'your_database.db'

def get_db():
		db = getattr(g, '_database', None)
		if db is None:
				db = g._database = sqlite3.connect(DATABASE)
		return db

@app.teardown_appcontext
def close_connection(exception):
		db = getattr(g, '_database', None)
		if db is not None:
				db.close()

@app.route('/')
def index():
		return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
		username = request.form.get('username')
		password = request.form.get('password')

		cursor = get_db().cursor()
		cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
		get_db().commit()

		return redirect(url_for('index'))

if __name__ == '__main__':
		app.run(debug=True)

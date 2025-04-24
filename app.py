from flask import Flask, render_template, request, session, url_for, redirect
import sqlite3

app = Flask(__name__)
app.secret_key = 'superctfkey' 


def get_db_connection():
    conn = sqlite3.connect('vuln.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    message = ''
    
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')

        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        print("[DEBUG] Login Query:", query)

        conn = get_db_connection()
        try:
            user = conn.execute(query).fetchone()
        except Exception as e:
            user = None
            message = f"SQL Error: {e}"
        finally:
            conn.close()

        if user:
            session['user'] = dict(user)
            username = user['username']
            if username != 'admin':
                message = (
                    "Welcome user, but this is not enough to get you what you need. "
                    "Inspect for some source."
                )
            else:
                message = "Your injection worked. But the system still holds its final source. Try Inspecting it."
            return render_template('dashboard.html', message=message)
        else:
            message = "Login failed. Try again."

    return render_template('login.html', message=message)


@app.route('/profile')
def profile():
    user = session.get('user')
    
    if not user:
        return render_template("profile.html", message="You are not logged in.", image="")

    username = user['username']
    
    if username == 'admin':
        return render_template("profile.html", 
                               message="Great Job! Here's your reward:<br><strong>flag{CTF_is_awesome}</strong>",
                               image=url_for('static', filename='images/flag_image.jpg'))
    else:
        return render_template("profile.html", 
                               message="You made it here... but not all users are admins. ",
                               image=url_for('static', filename='images/meme_image.jpg'))


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

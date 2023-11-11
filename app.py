from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random, secure key in a real application

users = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password == confirm_password:
            users.append({'username': username, 'password': password})
            flash('Account created successfully!', 'success')
            return redirect(url_for('signin'))
        else:
            flash('Passwords do not match. Please try again.', 'error')

    return render_template('signup.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        for user in users:
            if user['username'] == username and user['password'] == password:
                flash('Login successful!', 'success')
                return redirect(url_for('home'))

        flash('Invalid username or password. Please try again.', 'error')

    return render_template('signin.html')

if __name__ == '__main__':
    app.run(debug=True)

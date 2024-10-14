from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with your own secret key

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Here you can add your authentication logic
        if username == 'admin' and password == 'password':  # Dummy credentials
            flash('Login Successful!', 'success')
            return redirect(url_for('login'))
        else:
            flash('Login Failed. Check your credentials.', 'error')
    
    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


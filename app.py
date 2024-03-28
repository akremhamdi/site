from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = 'akrem'  # Replace with a secure secret key

@app.route('/')
def index():
    message = "Welcome to my home website!"
    logged_in = 'logged_in' in session  # Check if logged_in is set in session
    return render_template('index.html', message=message, logged_in=logged_in)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Simulate login validation (replace with actual validation)
        email = request.form['email']
        password = request.form['password']
        if email == 'akrem@email.com' and password == 'akrem':  # Replace with actual credentials
            session['logged_in'] = True  # Set logged_in in session
            return render_template('home.html')
        else:
            message = "Invalid email or password."
            return render_template('login.html', message=message)
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)  # Remove logged_in from session
    return render_template('index.html', message="You have been logged out.")  # Optional: Logout message

@app.route('/home')
def protected():
    if 'logged_in' not in session:
        return 'You need to be logged in to access this page!'
    return render_template('home.html')
@app.route('/camera')
def camera() :

    return render_template('cameraBtn.html')

@app.route('/garage')
def garage() :

    return render_template('garageBtn.html')

@app.route('/sleepinroom')
def sleepingroom() :

    return render_template('sleepingRoomBtn.html')
@app.route('/doorhall')
def doorhall() :

    return render_template('doorhallBtn.html')

@app.route('/bathroom')
def bathroom() :

    return render_template('bathroomBtn.html')

@app.route('/kitchen')
def kitchen() :

    return render_template('kitchenBtn.html')



if __name__ == '__main__':
    app.run(debug=True)

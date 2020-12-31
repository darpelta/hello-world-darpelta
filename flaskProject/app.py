from flask import Flask, render_template, url_for

app = Flask(__name__)


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

@app.route('/assignment8.html')
def assignment8():
    return render_template('assignment8.html', First_name='Dar', Last_name='Pelta', Favorite_songs_2020=['Holy','Come & Go', 'Exile'])


if __name__ == '__main__':
    app.run(debug=True)

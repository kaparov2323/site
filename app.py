from flask import Flask, render_template, url_for,  request, flash, redirect, session

app = Flask(__name__)
app.config["SECRET_KEY"] = 'fdgdfggf886hfghfg6h7f'

menu = [{'name':'Главная', 'url':'/'},
        {'name':'Установка', 'url':'install-flask'},
        {'name':'Обратная связь', 'url':'contact'},
        {'name':'Войти', 'url':'login'},
        {'name':'О сайте', 'url':'about'}]



@app.route("/")
def index():
    print(url_for('index'))
    return render_template('index.html', menu = menu)

@app.route("/about")
def about():
    print(url_for('about'))
    return render_template('about.html', title='О сайте', menu = menu)


@app.route("/contact", methods=["POST","GET"])
def contact():       
    if request.method == "POST":
        if len(request.form['username'])>2 and len(request.form['message'])>5:
            flash('Сообщение отправлено', category='success')
        else:
            flash('Ошибка отправки', category='error')
    
    return render_template('contact.html', title='Обратная связь', menu = menu)



@app.route('/login')
def login():
    return render_template('login.html', title="Авторизация", menu = menu)

@app.route("/profile/<username>")
def profile(username):
    return f'Профиль пользователя {username}'

@app.route("/install-flask")
def install_flask():
    return render_template('install_flask.html', title="Установка", menu = menu)


@app.errorhandler(404)
def pageNotFound(error):
    return render_template('page404.html', title='Страница не найдена', menu = menu)

if __name__== "__main__":
    app.run(debug=True)
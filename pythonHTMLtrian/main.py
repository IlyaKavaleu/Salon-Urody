from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from cloudipsp import Api, Checkout


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route('/buy/<int:price>')
def item_buy():
    pri = price.it.Item()
    for p in pri:

        from cloudipsp import Api, Checkout
        api = Api(merchant_id=1396424,    #мои данные
                  secret_key='test')      #Мой секретный ключ
        checkout = Checkout(api=api)
        data = {
            "currency": "pln",
            "amount": str(p)
        }
        url = checkout.url(data).get('checkout_url')
        return redirect(url)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vieworder')
def vieworder():
    return render_template('vieworder.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/auth')
def auth():
    return render_template('auth.html')

@app.route('/registr')
def registr():
    return render_template('registr.html')

@app.route('/vidymakijaza')
def vidymakijaza():
    return render_template('vidymakijaza.html')

@app.route('/myworks')
def myworks():
    return render_template('myworks.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/price')
def price():
    return render_template('price.html')




#makiajaz
@app.route('/makijaz')
def makijaz():
    return render_template('makijaz.html')

@app.route('/strobing')
def strobing():
    return render_template('strobing.html')

@app.route('/daystyle')
def daystyle():
    return render_template('daystyle.html')

@app.route('/eveningstyle')
def eveningstyle():
    return render_template('eveningstyle.html')

@app.route('/smokeyeyes')
def smokeyeyes():
    return render_template('smokeyeyes.html')

@app.route('/tumbler')
def tumbler():
    return render_template('tumbler.html')

@app.route('/lifting')
def lifting():
    return render_template('lifting.html')

@app.route('/marriege')
def marriege():
    return render_template('marriege.html')

@app.route('/retro')
def retro():
    return render_template('retro.html')

@app.route('/chicago')
def chicago():
    return render_template('chicago.html')

if __name__ == '__main__':
    app.run(debug=True)
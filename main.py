from flask import Flask, render_template, redirect, url_for
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\admin\\PycharmProjects\\pythonProject22Kantik\\test.db'
app.config['SECRET_KEY']='Alimzhan'
db = SQLAlchemy(app)




class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)

class ProductForm(FlaskForm):
    name = StringField('Название вашего товара')
    description = StringField('Описание')
    price = StringField('Цена за ваш товар')
    submit = SubmitField('Добавить ваш товар')



@app.route('/add',methods=['GET', 'POST'])
def add_products():
    form = ProductForm()
    if form.validate_on_submit():
        new_product = Product(name = form.name.data, description=form.description.data, price = form.price.data)
        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for('shop'))
    return render_template('add.html',form=form)


@app.route('/shop')
def shop():
    products = Product.query.all()
    return render_template('shop.html', products=products)

@app.route('/about')
def about():
    employees = [
        'dauxan',
        'tlek',
        'marlen',
        'kantemir'
    ]
    return render_template('about.html', employees=employees)



@app.route('/shop/<category_name>')
def category(category_name):
    return render_template('category.html', category=category_name)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

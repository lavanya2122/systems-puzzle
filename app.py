import datetime
import os

from flask import Flask, render_template, redirect, url_for
from forms import ItemForm
from models import Items
from database import db_session

app = Flask(__name__)
app.secret_key = os.environ['APP_SECRET_KEY']

@app.route("/", methods=('GET', 'POST'))
def add_item():
    form = ItemForm()
    if form.validate_on_submit():
        item = Items(name=form.name.data, quantity=form.quantity.data, description=form.description.data, date_added=datetime.datetime.now())
        db_session.add(item)
        db_session.commit()
        return redirect(url_for('success'))
    return render_template('index.html', form=form)

@app.route("/success")
def success():
    results = []
 
    qry = db_session.query(Items)
    for data in qry.all():
      ele = {
              "Item ID: " : str(data.id),
              "Item Name: " : str(data.name),
              "Item Quantity: " : str(data.quantity),
              "Item Description: ": str(data.description),
              "Item Date Added: ": str(data.date_added)
      }
      results.append(ele)
    return str(results)
  

if __name__ == '__main__':
    #if we want to expose 5001 port for flask app, then use below line
    #app.run(host='0.0.0.0', port=5001)
    app.run(host='0.0.0.0')

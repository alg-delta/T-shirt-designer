# app.py
from flask import Flask, render_template, redirect, url_for, session, request
from create_db import create_db
from models import db,Shirts,Print,Other


app = Flask(__name__)

# --- КОНФІГУРАЦІЯ FLASK ---
app.config['SECRET_KEY'] = 'your_super_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)



# --- МАРШРУТИ (ROUTES) ---

@app.route('/')
def home():
    """
    Головна сторінка додатку.
    """
    return render_template('index.html')
@app.route('/shirts', methods=["GET","POST"])
def shirt():
    if request.method == "POST":
        shirt_id=request.form.get("shirt")
        if shirt_id:
            session['shirt_id']=int(shirt_id)
            #print(session)
            return redirect(url_for('print'))

    shirts=Shirts.query.all()
    return render_template('step1.html',shirts=shirts)
@app.route('/prints',methods=["GET","POST"])
def print():
    if request.method=="POST":
        print_id=request.form.get("print")
        if print_id:
            session['print_id'] = int(print_id)
            return redirect(url_for('other'))
    prints=Print.query.all()
    return render_template('step2.html', prints=prints)
@app.route('/other',methods=["GET","POST"])
def other():
    #якщо не обрано суші
    if 'print_id' not in session:
        return redirect(url_for('print'))
    #post: коли натиснули кнопку далі
    if request.method=="POST":
        other_ids=[int(value) for value in request.form.getlist("other")]
        session['other_ids']=other_ids

        other_quantities={}
        for other_id in other_ids:
            count=request.form.get(f"count_{other_id}")
            other_quantities[other_id]=int(count) if int(count)>0 else 1
        session['other_quantities']=other_quantities
        name=request.form.get("name")
        phone=request.form.get("phone")
        comment=request.form.get("comment")
        session['name'] =name
        session['phone'] =phone
        session['comment'] =comment
        return redirect(url_for('sum'))
    #GET-коли входиш в сторінку

    others=Other.query.all()#отримуємо дані з суші
    selected_other_ids=session.get('other_ids',[])
    selected_quantities = {
        int(key): value for key, value in session.get('other_quantities', {}).items()
    }
    name=session.get('name',"")
    phone=session.get('phone',"")
    comment=session.get('comment',"")

    return render_template('step3.html',others=others,name=name,phone=phone,comment=comment,selected_other_ids=selected_other_ids,selected_quantities=selected_quantities)
@app.route('/sum_all', methods=["GET","POST"])
def sum():

    name=session.get('name','невказано')
    phone = session.get('phone', 'невказано')
    comment=session.get('comment','невказано')
    shirt=session.get('shirt_id')
    shirt=Shirts.query.get(shirt)
    print=session.get('print_id')
    print=Print.query.get(print)
    other_ids=session.get('other_ids',[])
    others=Other.query.filter(Other.id.in_(other_ids)).all()
    selected_quantities = {
        int(key): value for key, value in session.get('other_quantities', {}).items()
    }
    total_price=shirt.price+print.price
    for other in others:
        count=selected_quantities.get(other.id)
        total_price+=count*other.price
    return render_template('sum.html',total_price=total_price,name=name,phone=phone,comment=comment,shirt=shirt,print=print,others=others,selected_quantities=selected_quantities)
@app.route('/confirm', methods=["GET","POST"])
def confirm():
    session.clear()
    return redirect(url_for('home'))
# --- ЗАПУСК ДОДАТКА ---
if __name__ == '__main__':
    # create_db()
    app.run(debug=True)

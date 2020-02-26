from flask import Flask, render_template, request, session, redirect, url_for,flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'

class InfoForm(FlaskForm):
    breed = StringField('Enter the breed : ')
    submit = SubmitField('Submit')

@app.route('/',methods=['GET','POST'])
def homepage():
    form = InfoForm()
    if form.validate_on_submit():
        session['breed'] = form.breed.data
        flash(f"You just changed the breed to : {session['breed']}")
        return redirect(url_for('homepage'))
    return render_template('homepage.html',form=form)

if __name__=='__main__':
    app.run(debug=True)

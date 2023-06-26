from csv import reader
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap = Bootstrap5(app)

#  I need the following fields:
# Cafe name
# Google Maps URL
# Opening time
# Closing time
# Coffee rating
# WiFi strength
# Power socket availability.

class CafeForm(FlaskForm):
    cafe = StringField(label="Cafe name", validators=[DataRequired()])
    # TODO when I get back: Check why URL verification isn't working. 
    maps = StringField(label="Location", validators=[DataRequired(), URL(require_tld=True, message="Please enter a valid URL.")])
    open_time = StringField(label="Open", validators=[DataRequired()])
    close_time = StringField(label="Close", validators=[DataRequired()])
    coffee_rating = SelectField(
        label="Coffee",
        choices=["☕️", "☕️☕️", "☕️☕️☕️", "☕️☕️☕️☕️", "☕️☕️☕️☕️☕️"],
        validators=[DataRequired()]
    )
    wifi = SelectField(
        label="WiFi",
        choices=["💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"],
        validators=[DataRequired()]
    )
    socket = SelectField(
        label="Power",
        choices=["🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"],
        validators=[DataRequired()]
    )
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add')
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding="UTF-8") as csv_file:
        csv_data = reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)

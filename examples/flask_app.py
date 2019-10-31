"""
Example of using constrained types in a sign in form.
"""
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired

from typefactory import make_type
from typefactory.constraints import string
from typefactory.forms import make_string_field, make_password_field

UserName = make_type(str, "UserName", [string.MinLength(4), string.MaxLength(12), string.Pattern("[a-zA-Z]+")])
UserNameField = make_string_field(
    UserName, "UserNameField", render_kw=dict(title="Username must be between 4 and 12 alphabetical characters")
)

Password = make_type(str, "Password", [string.MinLength(8), string.MaxLength(256)])
PasswordField = make_password_field(Password, "PasswordField")


class SignInForm(FlaskForm):
    username = UserNameField("Username", [DataRequired()])
    password = PasswordField("Password", [DataRequired()])


app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"


@app.route("/", methods=["GET", "POST"])
def index():
    form = SignInForm()
    if form.validate_on_submit():
        print(form.username.data, type(form.username.data))
        print(form.password.data, type(form.password.data))
    return render_template("sign_in.html", form=form)


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="127.0.0.1")

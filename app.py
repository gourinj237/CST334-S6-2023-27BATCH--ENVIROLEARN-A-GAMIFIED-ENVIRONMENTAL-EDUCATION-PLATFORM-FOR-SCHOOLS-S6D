from flask import Flask,render_template 
from models import db, User
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app=Flask(__name__)


app.config['SECRET_KEY'] = 'secret123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "student_login"

@app.route('/')
def home():
    return render_template('role.html')


@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/carbon')
def carbon():
    return render_template('carbon.html')

if __name__=='__main__':
    app.run(debug=True)
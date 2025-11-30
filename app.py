from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import joblib
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here' # Change this for real apps
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# --- 1. LOAD AI MODEL ---
try:
    model = joblib.load('spam_model.pkl')
    cv = joblib.load('vectorizer.pkl')
except:
    print("⚠️ Model files not found. Run train_model.py first.")

# --- 2. DATABASE MODEL ---
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    date_joined = db.Column(db.DateTime, default=datetime.utcnow)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# --- 3. ROUTES ---

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        action = request.form['action'] # 'login' or 'register'

        if action == 'register':
            # Check if user exists
            if User.query.filter_by(username=username).first():
                flash('Username already exists.')
            else:
                new_user = User(
                    username=username, 
                    password=generate_password_hash(password, method='pbkdf2:sha256')
                )
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user)
                return redirect(url_for('detector'))

        elif action == 'login':
            user = User.query.filter_by(username=username).first()
            if user and check_password_hash(user.password, password):
                login_user(user)
                if user.is_admin:
                    return redirect(url_for('admin'))
                return redirect(url_for('detector'))
            else:
                flash('Invalid username or password.')

    return render_template('login.html')

@app.route('/detector', methods=['GET', 'POST'])
@login_required
def detector():
    prediction_text = ""
    css_class = ""
    original_text = ""

    if request.method == 'POST':
        original_text = request.form['message']
        data = [original_text]
        vect = cv.transform(data).toarray()
        prediction = model.predict(vect)
        
        if prediction[0] == 1:
            prediction_text = "⚠️ SPAM DETECTED"
            css_class = "result-spam"
        else:
            prediction_text = "✅ NOT SPAM (Safe)"
            css_class = "result-safe"

    return render_template('detector.html', prediction_text=prediction_text, css_class=css_class, original_text=original_text, name=current_user.username)

@app.route('/admin')
@login_required
def admin():
    if not current_user.is_admin:
        return redirect(url_for('detector'))
    
    users = User.query.all()
    total_users = len(users)
    return render_template('admin.html', users=users, total_users=total_users)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

# --- 4. CREATE DB & ADMIN ---
with app.app_context():
    db.create_all()
    # Create a default Admin if one doesn't exist
    if not User.query.filter_by(username='admin').first():
        admin_user = User(username='admin', password=generate_password_hash('admin123', method='pbkdf2:sha256'), is_admin=True)
        db.session.add(admin_user)
        db.session.commit()
        print("Admin created! User: admin | Pass: admin123")

if __name__ == '__main__':
    app.run(debug=True)
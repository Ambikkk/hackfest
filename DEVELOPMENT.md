# Development Guide - Placement Mentor Hub

## 🛠️ Setting Up Development Environment

### Prerequisites
- Python 3.8 or higher
- Git
- Code editor (VS Code recommended)

### Initial Setup

```bash
# Clone the repository
cd c:\hackfest\placement_mentor_hub

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create database with seed data
python seed_db.py

# Run application
python run.py
```

## 📂 Project Structure Guide

### `/app` - Main Application
- `__init__.py` - App factory and initialization
- `models.py` - SQLAlchemy database models
- `forms.py` - WTForms for form handling
- `decorators.py` - Role-based access decorators
- `utils.py` - Helper utilities and functions
- `ats_analyzer.py` - Resume ATS analysis algorithm

### `/app/blueprints` - Feature Modules
- `main.py` - Landing page and global routes
- `auth.py` - Authentication (login, register, logout)
- `admin.py` - Admin dashboard and management
- `trainer.py` - Trainer features
- `student.py` - Student features
- `api.py` - AJAX API endpoints

### `/app/templates` - HTML Templates
- `base.html` - Master layout with navigation
- `landing.html` - Home/landing page
- `/auth/` - Login and registration pages
- `/admin/` - Admin dashboard pages
- `/trainer/` - Trainer pages
- `/student/` - Student pages

### `/app/static` - Frontend Assets
- `/css/style.css` - Main stylesheet
- `/js/main.js` - JavaScript functions
- `/images/` - Image assets

## 🗄️ Database Models

### User Model
Base class for all users. Fields:
- id, name, email, password_hash, role
- profile_image, college, year_of_study
- created_at

### Trainer Model
Trainer profile. Fields:
- user_id (FK), price_per_month, bio, skills
- rating_average, rating_count, total_students_assisted
- is_active, admin_notes, created_at

### Student Model
Student profile with goal and skill tracking. Fields:
- user_id (FK), goal clarity, goal_title, selected_track
- Platform URLs (LeetCode, GitHub, etc.)
- Skill levels (DSA, DBMS, OS, CN, System Design, etc.)
- Tracking data (problems_solved, streak, hours, etc.)

### Key Relationship Models
- **TrainerStudentRelation**: Links trainers to students
- **SkillProgress**: Tracks individual skill topics
- **Doubt**: Q&A between users
- **ChatMessage**: Direct messages
- **Project/ProjectLog**: Project tracking
- **FocusSession**: Study session logging
- **Resume/ATSScan**: Resume management
- **JobApplication**: Job tracker
- **Badge**: Achievements

## 🔧 How to Add New Features

### 1. Add a New Model

Edit `/app/models.py`:
```python
class NewModel(db.Model):
    __tablename__ = 'new_model'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    # Add more fields
    
    def __repr__(self):
        return f'<NewModel {self.name}>'
```

### 2. Add a New Form

Edit `/app/forms.py`:
```python
class NewForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    # Add more fields
    submit = SubmitField('Submit')
```

### 3. Add a New Blueprint

Create `/app/blueprints/new_feature.py`:
```python
from flask import Blueprint, render_template

new_bp = Blueprint('new_feature', __name__)

@new_bp.route('/feature')
@login_required
def feature_page():
    return render_template('new_feature/page.html')

# Add more routes
```

Register in `/app/__init__.py`:
```python
from app.blueprints.new_feature import new_bp
app.register_blueprint(new_bp, url_prefix='/feature')
```

### 4. Add Templates

Create HTML file in appropriate directory under `/app/templates`:
```jinja2
{% extends "base.html" %}

{% block title %}Page Title{% endblock %}

{% block content %}
<div class="container">
    <!-- Your content here -->
</div>
{% endblock %}
```

### 5. Add Routes

Routes follow the pattern:
- Admin: `/admin/...`
- Trainer: `/trainer/...`
- Student: `/student/...`
- API: `/api/...`

## 🔐 Access Control

### Using Decorators

```python
from app.decorators import admin_required, trainer_required, student_required

@student_bp.route('/page')
@student_required
def student_only_page():
    return render_template('student/page.html')
```

### Checking Current User

In routes:
```python
from flask_login import current_user

if current_user.is_authenticated:
    student = current_user.student  # For student users
    trainer = current_user.trainer  # For trainer users
```

In templates:
```jinja2
{% if current_user.is_authenticated %}
    {% if current_user.role == 'STUDENT' %}
        <!-- Student-specific content -->
    {% endif %}
{% endif %}
```

## 📝 Common Tasks

### Add a New API Endpoint

Edit `/app/blueprints/api.py`:
```python
@api_bp.route('/data/<int:id>', methods=['GET'])
@login_required
def get_data(id):
    from app.models import SomeModel
    item = SomeModel.query.get_or_404(id)
    return jsonify({'data': item.name})
```

### Query the Database

```python
# Get one record
user = User.query.filter_by(email='test@example.com').first()

# Get multiple records
users = User.query.filter_by(role='STUDENT').all()

# Use relationships
student = Student.query.get(1)
trainer = student.trainer_relations[0].trainer_rel

# Aggregations
count = User.query.filter_by(role='ADMIN').count()
```

### Create Database Records

```python
from app.models import db, User

user = User(
    name='John',
    email='john@test.com',
    role='STUDENT'
)
user.set_password('password123')
db.session.add(user)
db.session.commit()
```

### Handle Forms

In route:
```python
from app.forms import MyForm

@app.route('/page', methods=['GET', 'POST'])
def my_page():
    form = MyForm()
    
    if form.validate_on_submit():
        # Process form
        flash('Success!', 'success')
        return redirect(url_for('main.index'))
    
    return render_template('page.html', form=form)
```

In template:
```jinja2
<form method="POST">
    {{ form.hidden_tag() }}
    
    {{ form.field_name.label() }}
    {{ form.field_name() }}
    {% if form.field_name.errors %}
        <div class="alert alert-danger">
            {% for error in form.field_name.errors %}
                {{ error }}
            {% endfor %}
        </div>
    {% endif %}
    
    {{ form.submit() }}
</form>
```

## 🎨 Styling Guide

### Color Scheme
```css
:root {
    --primary-color: #667eea;     /* Purple-blue */
    --secondary-color: #764ba2;   /* Purple */
    --success-color: #28a745;     /* Green */
    --danger-color: #dc3545;      /* Red */
    --warning-color: #ffc107;     /* Yellow */
    --info-color: #17a2b8;        /* Cyan */
}
```

### Common Classes
```css
.kpi-card       /* KPI card style */
.card           /* Generic card */
.btn-primary    /* Primary button */
.btn-success    /* Success button */
.badge          /* Badge pill style */
.progress-bar   /* Progress bar */
```

### Animations
```css
.animate-fade-in       /* Fade in animation */
.animate-slide-up      /* Slide up animation */
.shadow                /* Drop shadow */
```

## 🧪 Testing

### Manual Testing Checklist
- [ ] Login with all user roles
- [ ] Check role-specific dashboards
- [ ] Test form validation
- [ ] Verify database operations
- [ ] Check responsive design
- [ ] Test animations
- [ ] Verify all links work

### Using Browser DevTools
1. Open DevTools (F12)
2. Check Console for JavaScript errors
3. Check Network for slow requests
4. Use Elements to inspect HTML
5. Use Application to check localStorage/sessions

## 🚀 Performance Tips

### Database
```python
# Don't:
for user in User.query.all():
    print(user.trainer.name)  # N+1 query problem

# Do:
users = User.query.filter_by(role='STUDENT').all()
# Or use eager loading:
users = User.query.options(db.joinedload(User.trainer)).all()
```

### Templates
```jinja2
<!-- Cache blocks that don't change -->
{% cache 3600 %}
    { expensive_template %}
{% endcache %}
```

### Frontend
- Minify CSS/JS for production
- Optimize images
- Use CDN for external libraries
- Lazy load images
- Compress assets

## 🐛 Debugging

### Enable Debug Mode
```python
app.run(debug=True)
```

### Database Debugging
```python
from sqlalchemy import event
from sqlalchemy.engine import Engine
import logging

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
```

### Print Debugging
```python
from flask import current_app
current_app.logger.debug('Debug message')
```

## 📦 Deploying to Production

### Prepare for Production
1. Set `DEBUG=False` in config
2. Change `SECRET_KEY` to random value
3. Use PostgreSQL instead of SQLite
4. Add environment variables
5. Set `SESSION_COOKIE_SECURE=True`

### Deploy with Gunicorn
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 run:app
```

### Deploy to Heroku
```bash
# Create Procfile
echo "web: gunicorn run:app" > Procfile

# Create runtime.txt
echo "python-3.9.7" > runtime.txt

# Push to Heroku
git push heroku main
```

## 🤝 Contributing

### Code Style
- Use PEP 8 for Python
- Use meaningful variable names
- Add docstrings to functions
- Comment complex logic
- Keep functions small (single responsibility)

### Before Committing
- Test your changes
- Check for errors with browser console
- Verify database operations
- Run seed_db.py after schema changes
- Update documentation

## 📚 Resources

- Flask Documentation: https://flask.palletsprojects.com/
- SQLAlchemy ORM: https://docs.sqlalchemy.org/
- Flask-Login: https://flask-login.readthedocs.io/
- Bootstrap 5: https://getbootstrap.com/
- Chart.js: https://www.chartjs.org/

## 🎯 Next Features to Add

Priority: High
- [ ] Real-time notifications with WebSockets
- [ ] Email notifications
- [ ] File upload for resumes and profile images
- [ ] Advanced search and filtering
- [ ] Payment integration

Priority: Medium
- [ ] SMS alerts
- [ ] Calendar integration
- [ ] Video call integration
- [ ] API authentication (JWT)
- [ ] Admin reports export

Priority: Low
- [ ] AI-powered recommendations
- [ ] Live coding sessions
- [ ] Interview prep modules
- [ ] Mobile app

---

**Happy Coding!** 🚀

Questions? Check the README.md and QUICKSTART.md files.

# Placement Mentor Hub - Quick Start Guide

## 🚀 Super Quick Setup (5 minutes)

### Step 1: Install Dependencies
```bash
cd c:\hackfest\placement_mentor_hub
pip install -r requirements.txt
```

### Step 2: Seed Database (Optional but Recommended)
```bash
python seed_db.py
```
This creates demo data including 1 admin, 3 trainers, and 10 students.

### Step 3: Run the App
```bash
python run.py
```

### Step 4: Open in Browser
```
http://localhost:5000
```

## 👤 Demo Login Credentials

| Role | Email | Password |
|------|-------|----------|
| Admin | admin@test.com | password123 |
| Trainer | trainer1@test.com | password123 |
| Student | student1@test.com | password123 |

Or register a new student account!

## 🎯 What to Try First

### As a Student:
1. Go to Dashboard
2. Click "Update Goal" to set your career path
3. View Skills progress
4. Find Trainers and request mentorship
5. Start a Focus Timer session
6. Build a Resume and check ATS score
7. Add Job Applications

### As a Trainer:
1. Dashboard to see stats
2. View your Students
3. Toggle "Go Online" status
4. View Doubts from students
5. Edit your Profile

### As Admin:
1. Dashboard for platform overview
2. Manage Trainers (add new, view details)
3. View all Students and their analytics
4. Check Global Analytics

## 📱 Features Included

✅ User Authentication (Login/Register)
✅ Role-based Dashboards (Admin/Trainer/Student)
✅ Skill Progress Tracking
✅ Trainer Mentorship Matching
✅ Doubt/Chat System
✅ Project Tracker with Logs
✅ Focus Timer with Session Tracking
✅ Resume Builder
✅ ATS Resume Checker
✅ Job Application Tracker (Kanban)
✅ Achievement Badges
✅ Responsive Design
✅ Beautiful Animations
✅ KPI Cards & Charts Ready
✅ SQLite Database

## 🗂️ Project Structure

```
placement_mentor_hub/
├── app/                          # Main application package
│   ├── models.py                 # Database models (User, Student, Trainer, etc.)
│   ├── forms.py                  # WTForms for all pages
│   ├── decorators.py             # Role-based access decorators
│   ├── utils.py                  # Helper functions
│   ├── ats_analyzer.py           # ATS scoring algorithm
│   ├── blueprints/               # Flask blueprints
│   │   ├── main.py               # Landing page
│   │   ├── auth.py               # Login/Register
│   │   ├── admin.py              # Admin features
│   │   ├── trainer.py            # Trainer features
│   │   ├── student.py            # Student features
│   │   └── api.py                # AJAX API endpoints
│   ├── templates/                # Jinja2 templates
│   │   ├── base.html             # Master layout
│   │   ├── landing.html          # Home page
│   │   ├── auth/                 # Login/Register pages
│   │   ├── admin/                # Admin pages
│   │   ├── trainer/              # Trainer pages
│   │   └── student/              # Student pages
│   └── static/                   # CSS, JS, Images
│       ├── css/style.css         # Custom styles
│       └── js/main.js            # JavaScript
├── config.py                     # Flask configuration
├── run.py                        # Start application here
├── seed_db.py                    # Create sample data
├── requirements.txt              # Python packages
└── README.md                     # Full documentation
```

## 🔧 Customization Tips

### Change Database Location
Edit `config.py`:
```python
SQLALCHEMY_DATABASE_URI = 'sqlite:///path/to/your/db.db'
```

### Add More Demo Data
Edit `seed_db.py` and run it again after clearing the database:
```bash
rm placement_mentor_hub.db
python seed_db.py
```

### Change Port
In `run.py`:
```python
app.run(port=5001)  # Change to any port
```

### Customize Colors
Edit `app/static/css/style.css`:
```css
:root {
    --primary-color: #667eea;    /* Change these */
    --secondary-color: #764ba2;
    /* ... */
}
```

## 📊 Database Models Overview

The app uses 18 database tables:
- **User**: Authentication & profile
- **Trainer**: Mentor profiles
- **Student**: Learner profiles
- **TrainerStudentRelation**: Mentorship links
- **SkillProgress**: Skill tracking
- **Doubt**: Q&A between trainer-student
- **ChatMessage**: Direct messaging
- **Project**: Student projects
- **ProjectLog**: Daily progress
- **FocusSession**: Study sessions
- **Resume**: Resume storage
- **ATSScan**: ATS scoring
- **JobApplication**: Job tracker
- **Badge**: Achievements
- **CoverLetter**: Cover letters
- **Notification**: User notifications
- Plus supporting models

## 🎨 Beautiful UI Features

- ✨ Gradient backgrounds (purple/indigo)
- 🎯 Animated KPI cards
- 📊 Smooth progress bars
- 🔴 Notifications & alerts
- 📱 Responsive sidebar
- 🎭 Hover animations
- 🎪 Card elevation effects
- 📈 Counter animations
- 🌈 Color-coded status badges

## 🔐 Security Features

- Password hashing with Werkzeug
- CSRF protection with Flask-WTF
- SQL injection protection (SQLAlchemy)
- Session-based authentication
- Role-based access control (RBAC)

## ⚡ Performance Notes

- SQLite suitable for up to 10k+ users
- Consider PostgreSQL for production
- Database indexes on key fields
- Efficient query relationships

## 🆘 Help & Support

### Common Issues

**Port 5000 already in use?**
```bash
python run.py --port 5001
```

**Database errors?**
```bash
# Delete and recreate
rm placement_mentor_hub.db
python seed_db.py
```

**Dependencies not installing?**
```bash
# Use Python 3.8+ and pip latest
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 📚 Next Steps

1. ✅ Run the app
2. 📝 Log in with demo credentials
3. 🎨 Explore all dashboards
4. 💡 Customize colors/text
5. 🚀 Add your features
6. 📤 Deploy on cloud (Heroku, AWS, etc.)

## 🎓 Learning from This Project

This codebase teaches:
- Flask app factory pattern
- Blueprint modular architecture
- SQLAlchemy ORM relationships
- Flask-Login authentication
- WTForms validation
- Jinja2 template inheritance
- Bootstrap 5 responsive design
- AJAX/Fetch API integration
- Role-based access control
- Database schema design

## 🚀 Ready to Deploy?

For production:
1. Change `SECRET_KEY` in config.py
2. Set `DEBUG=False`
3. Use a WSGI server (Gunicorn)
4. Add HTTPS/SSL
5. Use PostgreSQL instead of SQLite
6. Add environment variables

Example deployment with Gunicorn:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 run:app
```

---

**Happy Coding! 🎉**

For full documentation, see README.md

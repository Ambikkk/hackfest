# Placement Mentor Hub

A comprehensive full-stack web application for connecting students with mentors for placement preparation, skill tracking, and career guidance.

## 🎯 Features

### For Students
- **Dashboard**: Real-time progress tracking with KPIs
- **Skill Progress Tracking**: Monitor development in DSA, DBMS, OS, CN, System Design, and more
- **Trainer Matching**: Find and connect with experienced mentors
- **Focus Timer**: Track coding hours with categorized focus sessions
- **Project Tracker**: Manage projects with daily progress logs and timelines
- **Resume Builder**: Create ATS-friendly resumes with live preview
- **ATS Checker**: Analyze resume compatibility with job descriptions
- **Job Tracker**: Kanban-style job application board
- **Chat & Doubts**: Direct communication with assigned trainers
- **Achievement Badges**: Earn badges for milestones (problems solved, streaks, etc.)

### For Trainers
- **Student Management**: View and analyze all mentored students
- **Active Status Toggle**: Go online/offline for real-time availability
- **Doubt Management**: Handle student questions with categorization
- **Performance Analytics**: Track rating, students helped, response times
- **Direct Messaging**: Chat with students for guidance and support
- **Profile Management**: Update skills, pricing, and bio

### For Admins
- **Dashboard Analytics**: Real-time metrics on platform activity
- **Trainer Management**: Add, edit, and monitor trainers
- **Student Analytics**: Deep dive into student progress and performance
- **Global Analytics**: Platform-wide insights and trends
- **Notifications**: Central hub for platform activities

## 🛠️ Tech Stack

### Backend
- **Framework**: Flask with Blueprints
- **Database**: SQLite3 with SQLAlchemy ORM
- **Authentication**: Flask-Login with Werkzeug password hashing
- **Forms**: Flask-WTF

### Frontend
- **Templates**: Jinja2
- **CSS**: Bootstrap 5 + custom CSS with animations
- **JavaScript**: Vanilla JS with AJAX
- **Charts**: Chart.js for data visualization

## 📦 Installation

### Prerequisites
- Python 3.8+
- pip

### Setup

1. **Clone/Download the project**
   ```bash
   cd c:\hackfest\placement_mentor_hub
   ```

2. **Create virtual environment** (Optional but recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Seed the database** (Optional - includes demo data)
   ```bash
   python seed_db.py
   ```

5. **Run the application**
   ```bash
   python run.py
   ```

6. **Access the app**
   Open your browser and navigate to: `http://localhost:5000`

## 📋 Demo Credentials

After running `seed_db.py`, you can login with:

**Admin**
- Email: `admin@test.com`
- Password: `password123`

**Trainer**
- Email: `trainer1@test.com`
- Password: `password123`

**Student**
- Email: `student1@test.com`
- Password: `password123`

## 📁 Project Structure

```
placement_mentor_hub/
├── app/
│   ├── __init__.py           # App factory
│   ├── models.py             # SQLAlchemy models
│   ├── forms.py              # WTForms
│   ├── decorators.py         # Role-based decorators
│   ├── utils.py              # Helper functions
│   ├── ats_analyzer.py       # ATS scoring logic
│   ├── blueprints/
│   │   ├── main.py           # Landing page
│   │   ├── auth.py           # Login/Register
│   │   ├── admin.py          # Admin dashboard
│   │   ├── trainer.py        # Trainer features
│   │   ├── student.py        # Student features
│   │   └── api.py            # AJAX endpoints
│   ├── templates/
│   │   ├── base.html         # Base layout
│   │   ├── landing.html      # Landing page
│   │   ├── auth/             # Auth templates
│   │   ├── admin/            # Admin templates
│   │   ├── trainer/          # Trainer templates
│   │   └── student/          # Student templates
│   └── static/
│       ├── css/
│       │   └── style.css     # Custom styles
│       ├── js/
│       │   └── main.js       # Main JavaScript
│       └── images/           # Assets
├── config.py                 # Configuration
├── run.py                    # Application entry point
├── seed_db.py                # Database seeding
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## 🗄️ Database Models

### Core Models
- **User**: Base user model with role-based access (ADMIN, TRAINER, STUDENT)
- **Trainer**: Trainer profile with pricing, rating, and skills
- **Student**: Student profile with goals, skills, and progress metrics

### Relationship Models
- **TrainerStudentRelation**: Mentorship relationships with interaction tracking
- **SkillProgress**: Individual skill and topic progress tracking

### Feature Models
- **Doubt**: Q&A between trainer and student
- **ChatMessage**: Direct messaging
- **Project**: Student project tracking
- **ProjectLog**: Daily progress logs
- **FocusSession**: Coding session tracking
- **Resume**: Resume storage and management
- **ATSScan**: Resume-to-job-description scoring
- **JobApplication**: Job application tracker
- **Badge**: Achievement system
- **Notification**: User notifications
- **CoverLetter**: Cover letter drafts

## 🎨 UI/UX Features

- **Responsive Design**: Mobile, tablet, and desktop support
- **Modern Sidebar Navigation**: With smooth transitions
- **Animated KPI Cards**: Counter animations on dashboard
- **Smooth Gradients**: Professional visual hierarchy
- **Interactive Forms**: Validation with Bootstrap styling
- **Progress Bars**: Skill level visualization
- **Kanban Board**: Drag-and-drop job tracking (HTML structure ready)
- **Toast Notifications**: Real-time feedback
- **Animations**: CSS transitions and keyframe animations

## 🚀 Key Endpoints

### Auth
- `GET/POST /auth/login` - User login
- `GET/POST /auth/register` - Student registration
- `GET /auth/logout` - User logout

### Admin
- `GET /admin/dashboard` - Admin overview
- `GET /admin/trainers` - Trainer management
- `GET /admin/students` - Student list and analytics
- `GET /admin/analytics` - Global analytics

### Trainer
- `GET /trainer/dashboard` - Trainer overview
- `GET /trainer/students` - Student list
- `GET /trainer/students/<id>` - Student details
- `GET /trainer/messages/<id>` - Chat interface
- `GET /trainer/doubts` - Doubt management

### Student
- `GET /student/dashboard` - Student overview
- `GET /student/skills` - Skill tracking
- `GET /student/projects` - Project management
- `GET /student/focus` - Focus timer
- `GET /student/resumes` - Resume builder
- `GET /student/ats-checker` - ATS scoring
- `GET /student/job-tracker` - Job applications
- `GET /student/trainers` - Find trainers

### API
- `GET /api/notifications` - Get user notifications
- `GET /api/stats/dashboard` - Dashboard statistics
- `GET /api/doubts/unread` - Unread doubts
- Various chart endpoints for data visualization

## 🔐 Role-Based Access Control

- **Anonymous**: Can view landing page, login, and register
- **ADMIN**: Full platform access
- **TRAINER**: Student management, messaging, analytics
- **STUDENT**: Personal dashboard, skill tracking, trainer search, job tools

## 🎓 ATS Analyzer Algorithm

The built-in ATS checker analyzes resumes by:
1. Extracting hard skills (programming languages, frameworks, tools)
2. Extracting soft skills (communication, leadership, teamwork)
3. Comparing against job description keywords
4. Checking format quality (sections, metrics, length)
5. Generating actionable suggestions

Scoring: 50% hard skills match + 20% soft skills + 30% format quality

## 📊 Data Visualization

The platform includes ready-to-use Chart.js integrations for:
- Streak progression graphs
- Problems solved over time
- Focus time by category
- Doubt frequency charts
- Student performance metrics

## 🔧 Configuration

Edit `config.py` to customize:
- Database location
- Secret key
- Session timeout
- Debug mode
- Security settings

## 🚦 Running in Production

1. Set environment variables:
   ```bash
   export FLASK_ENV=production
   export SECRET_KEY=your-secret-key
   ```

2. Use a production WSGI server:
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:8000 run:app
   ```

3. Set `SESSION_COOKIE_SECURE=True` in config.py

## 📝 Sample Data

The `seed_db.py` script creates:
- 1 Admin user
- 3 Trainers (1 free, 2 paid)
- 10 Students
- Trainer-student relationships
- Sample skill progress, projects, resumes, and job applications
- Mock focus sessions and badges

## 🐛 Troubleshooting

### Database Issues
```bash
# Reset database
rm placement_mentor_hub.db
python seed_db.py
```

### Import Errors
```bash
# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

### Port Already in Use
```bash
# Run on different port
python run.py --port 5001
```

## 📚 Learning Resources

The codebase demonstrates:
- Flask blueprints for modular architecture
- SQLAlchemy ORM relationships
- Flask-Login user authentication
- WTForms form handling and validation
- Jinja2 templating with inheritance
- Bootstrap 5 responsive design
- AJAX/fetch API integration
- Role-based access control
- Database modeling best practices

## 🤝 Contributing

This is a hackathon project. Feel free to:
- Add more features
- Improve UI/UX
- Optimize database queries
- Add more analytics
- Implement real-time notifications with WebSockets
- Add file upload for profile pictures and resumes

## 📄 License

This project is open source and available for educational purposes.

## 🎉 Enjoy Building!

Happy coding and best of luck with your placements! 🚀

---

**Built with ❤️ for Hackfest 2025**

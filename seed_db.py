"""
Database seeding script for Placement Mentor Hub
Populates the database with sample data for demo purposes
"""
from app import create_app, db
from app.models import (User, Trainer, Student, TrainerStudentRelation, SkillProgress,
                       Doubt, Project, ProjectLog, FocusSession, Resume, ATSScan, 
                       JobApplication, Badge)
from datetime import datetime, timedelta
import json

def seed_database():
    """Populate database with sample data"""
    
    app = create_app('development')
    
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()
        
        print("Seeding database...")
        
        # 1. Create Admin User
        admin = User(
            name="Admin User",
            email="admin@test.com",
            role="ADMIN",
            college="Test University",
            year_of_study=4
        )
        admin.set_password("password123")
        db.session.add(admin)
        db.session.flush()
        print("✓ Admin created")
        
        # 2. Create Trainer Users
        trainers_data = [
            {
                'name': 'Rahul Singh',
                'email': 'trainer1@test.com',
                'price': 0,
                'bio': 'Senior SDE at Tech Company. Specializing in DSA and System Design.',
                'skills': 'Python, JavaScript, DSA, System Design, Backend'
            },
            {
                'name': 'Priya Sharma',
                'email': 'trainer2@test.com',
                'price': 499,
                'bio': 'Full Stack Developer with 5+ years experience.',
                'skills': 'React, Node.js, MongoDB, AWS, Web Development'
            },
            {
                'name': 'Amit Kumar',
                'email': 'trainer3@test.com',
                'price': 299,
                'bio': 'Data Science Expert and AI Enthusiast.',
                'skills': 'Python, Machine Learning, Data Science, Statistics'
            }
        ]
        
        trainer_users = []
        for t_data in trainers_data:
            user = User(
                name=t_data['name'],
                email=t_data['email'],
                role='TRAINER'
            )
            user.set_password('password123')
            db.session.add(user)
            db.session.flush()
            
            trainer = Trainer(
                user_id=user.id,
                price_per_month=t_data['price'],
                bio=t_data['bio'],
                skills=t_data['skills'],
                is_active=True,
                rating_average=4.5 if t_data['price'] == 0 else 4.3,
                rating_count=15,
                total_students_assisted=8
            )
            db.session.add(trainer)
            trainer_users.append(trainer)
        
        db.session.flush()
        print(f"✓ {len(trainers_data)} Trainers created")
        
        # 3. Create Student Users
        student_names = [
            'John Doe', 'Sarah Johnson', 'Mike Chen', 'Akshay Patel',
            'Neha Gupta', 'Arjun Verma', 'Priya Singh', 'Rohan Kumar',
            'Anjali Reddy', 'Vishal Chopra'
        ]
        
        student_users = []
        for i, name in enumerate(student_names):
            user = User(
                name=name,
                email=f'student{i+1}@test.com',
                role='STUDENT',
                college='Tech University',
                year_of_study=3 + (i % 2)  # Mix of 3rd and 4th year
            )
            user.set_password('password123')
            db.session.add(user)
            db.session.flush()
            
            student = Student(
                user_id=user.id,
                has_goal_clarity=True,
                goal_title='SDE at FAANG' if i % 2 == 0 else 'Backend Engineer',
                selected_track='Backend' if i % 2 == 0 else 'Full Stack',
                leetcode_rating=1200 + (i * 100),
                leetcode_problems_solved=50 + (i * 10),
                leetcode_daily_streak=5 + (i % 7),
                total_code_hours=80 + (i * 20),
                consistency_score=75 + (i * 2),
                dsa_level=3 + (i % 3),
                dbms_level=3 + (i % 2),
                os_level=2 + (i % 3),
                cn_level=2 + (i % 2),
                system_design_level=1 + (i % 3),
                soft_skills_level=3 + (i % 3),
                aptitude_level=3 + (i % 2)
            )
            db.session.add(student)
            student_users.append(student)
        
        db.session.flush()
        print(f"✓ {len(student_names)} Students created")
        
        # 4. Create Trainer-Student Relations
        for i, student in enumerate(student_users[:8]):
            trainer = trainer_users[i % 3]
            relation = TrainerStudentRelation(
                trainer_id=trainer.id,
                student_id=student.id,
                is_active=True,
                started_at=datetime.utcnow() - timedelta(days=30),
                total_doubts_asked=5 + i,
                total_doubts_answered=4 + i,
                student_rating_for_trainer=4.5 - (i % 2) * 0.5
            )
            db.session.add(relation)
        
        db.session.flush()
        print("✓ Trainer-Student Relations created")
        
        # 5. Create Skill Progress
        for student in student_users:
            skills = [
                ('DSA', 'Arrays & Strings'),
                ('DSA', 'Trees & Graphs'),
                ('DBMS', 'SQL Queries'),
                ('OS', 'Process Management'),
                ('System Design', 'Scalability'),
            ]
            for skill_name, topic in skills:
                sp = SkillProgress(
                    student_id=student.id,
                    skill_name=skill_name,
                    topic_name=topic,
                    problem_count=20 + (student.id % 10),
                    done_problem_count=10 + (student.id % 5),
                )
                db.session.add(sp)
        
        db.session.flush()
        print("✓ Skill Progress created")
        
        # 6. Create Doubts
        for i, student in enumerate(student_users[:5]):
            relation = TrainerStudentRelation.query.filter_by(student_id=student.id).first()
            if relation:
                doubt = Doubt(
                    from_user_id=student.user_id,
                    to_user_id=relation.trainer_rel.user_id,
                    relation_id=relation.id,
                    text=f"How do I solve problem {10+i}? I'm stuck on the edge case.",
                    type='DOUBT'
                )
                db.session.add(doubt)
        
        db.session.flush()
        print("✓ Doubts created")
        
        # 7. Create Projects
        for i, student in enumerate(student_users):
            project = Project(
                student_id=student.id,
                title=f"Project {i+1}: E-Commerce Platform" if i % 2 == 0 else f"Project {i+1}: Chat Application",
                description="Building a scalable web application",
                tech_stack="React, Node.js, MongoDB, AWS",
                target_date=datetime.utcnow() + timedelta(days=30)
            )
            db.session.add(project)
            db.session.flush()
            
            # Add project logs
            for day in range(5):
                log = ProjectLog(
                    project_id=project.id,
                    date=datetime.utcnow().date() - timedelta(days=4-day),
                    summary=f"Day {day+1}: Completed feature {day+1}",
                    hours_spent=2 + (day % 3)
                )
                db.session.add(log)
        
        db.session.flush()
        print("✓ Projects created")
        
        # 8. Create Focus Sessions
        for i, student in enumerate(student_users):
            for day in range(3):
                session = FocusSession(
                    student_id=student.id,
                    started_at=datetime.utcnow() - timedelta(days=day),
                    ended_at=datetime.utcnow() - timedelta(days=day, hours=-2),
                    duration_minutes=120,
                    label=['DSA', 'DBMS', 'Projects'][day % 3]
                )
                db.session.add(session)
        
        db.session.flush()
        print("✓ Focus Sessions created")
        
        # 9. Create Resumes
        for i, student in enumerate(student_users[:5]):
            resume = Resume(
                student_id=student.id,
                title=f"Resume v{i+1}",
                raw_text=f"""
                {student.user.name}
                Email: {student.user.email}
                
                SUMMARY
                Passionate developer with strong DSA skills and {student.total_code_hours} hours of coding experience.
                
                SKILLS
                Languages: Python, JavaScript, Java
                Frameworks: React, Node.js, Django
                Databases: SQL, MongoDB, PostgreSQL
                Tools: Git, Docker, AWS
                
                EXPERIENCE
                Junior Developer Intern - Tech Company
                - Developed web features using React
                - Solved 50+ DSA problems
                
                EDUCATION
                B.Tech in Computer Science
                {student.user.college if student.user.college else 'University'}
                
                PROJECTS
                E-Commerce Platform - React, Node.js, MongoDB
                Chat Application - Socket.io, Express
                
                ACHIEVEMENTS
                Solved {student.leetcode_problems_solved} LeetCode problems
                {student.leetcode_daily_streak}-day coding streak
                """,
                template_type='simple'
            )
            db.session.add(resume)
            db.session.flush()
            
            # Create ATS Scan
            scan = ATSScan(
                resume_id=resume.id,
                job_title="Senior Software Engineer",
                job_description_text="Looking for experienced Python/JavaScript developer...",
                score_overall=75 + (i * 3),
                score_hard_skills=80,
                score_soft_skills=70,
                score_format=75,
                missing_keywords=json.dumps(['System Design', 'Microservices']),
                suggestions=json.dumps(['Add more metrics', 'Improve formatting'])
            )
            db.session.add(scan)
        
        db.session.flush()
        print("✓ Resumes and ATS Scans created")
        
        # 10. Create Job Applications
        for i, student in enumerate(student_users[:6]):
            companies = [
                ('Google', 'Software Engineer'),
                ('Amazon', 'Backend Engineer'),
                ('Microsoft', 'Full Stack Developer'),
                ('Apple', 'iOS Developer'),
                ('Flipkart', 'SDE'),
                ('Swiggy', 'Backend Engineer')
            ]
            
            for j in range(2):
                company, role = companies[(i + j) % len(companies)]
                app = JobApplication(
                    student_id=student.id,
                    company=company,
                    role=role,
                    location='Bangalore, India',
                    applied_date=datetime.utcnow().date() - timedelta(days=j*5),
                    status=['TO_APPLY', 'APPLIED', 'ONLINE_TEST'][j % 3],
                    ats_score_at_apply=75 + (i * 2)
                )
                db.session.add(app)
        
        db.session.flush()
        print("✓ Job Applications created")
        
        # 11. Create Badges
        badge_data = [
            ('leet_1', 'First Problem', 'Solved your first LeetCode problem'),
            ('leet_50', 'Halfway There', 'Solved 50 LeetCode problems'),
            ('streak_3', '3-Day Streak', 'Maintained 3-day coding streak'),
            ('streak_7', 'Week Warrior', 'Maintained 7-day coding streak'),
        ]
        
        for i, student in enumerate(student_users[:5]):
            for j in range(min(2 + (i % 2), len(badge_data))):
                badge_key, title, desc = badge_data[j]
                badge = Badge(
                    student_id=student.id,
                    badge_key=badge_key,
                    title=title,
                    description=desc,
                    unlocked_at=datetime.utcnow() - timedelta(days=10-i)
                )
                db.session.add(badge)
        
        db.session.commit()
        print("✓ Badges created")
        print("\n✅ Database seeded successfully!")
        print("\nDemo Credentials:")
        print("  Admin: admin@test.com / password123")
        print("  Trainer: trainer1@test.com / password123")
        print("  Student: student1@test.com / password123")

if __name__ == '__main__':
    seed_database()

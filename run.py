"""
Run script for Placement Mentor Hub
"""
import os
from app import create_app, db

if __name__ == '__main__':
    # Create app
    app = create_app(os.environ.get('FLASK_ENV', 'development'))
    
    # Initialize database
    with app.app_context():
        db.create_all()
    
    # Run app
    app.run(debug=True, host='0.0.0.0', port=5000)

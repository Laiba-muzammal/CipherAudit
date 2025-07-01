from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # 🟡 App ke bina bana lo instance

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    
    db.init_app(app)  # 🟢 Yahan bind karo
    
    return app

if __name__=='__main__':
    app = create_app()  
    app.run(debug=True)
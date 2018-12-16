from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Stage(db.Model):
    __tablename__ = 'meditstages'
    uid = db.Column(db.Integer, primary_key = True)
    stage = db.Column(db.String(100))
    description = db.Column(db.String(1000))
    
    def __init__(self, stage, description):
        self.stage = stage.title()
        self.description = description.lower()
        
    
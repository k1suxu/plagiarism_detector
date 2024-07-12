from . import db
from datetime import datetime

class PlagiarismCheck(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code1 = db.Column(db.Text, nullable=False)
    code2 = db.Column(db.Text, nullable=False)
    similarity_score = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<PlagiarismCheck {self.id}>'
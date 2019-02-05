from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

# define your models classes hereafter
# PUBLICATION TABLE
class Publication(db.Model):
    __tablename__ = 'publication'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return 'The id is {}, Name is is {}'.format(self.id, self.name)
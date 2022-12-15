from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate


# 目前文件路徑
pjdir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# 新版本的部份預設為none，會有異常，再設置True即可。
# 追蹤改變的信號，會消耗額外的記憶體
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(pjdir, 'data.sqlite')

db = SQLAlchemy(app)
Migrate(app,db)

# Many-to-Many
tags = db.Table('tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
    db.Column('page_id', db.Integer, db.ForeignKey('page.id'), primary_key=True)
)

class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tags = db.relationship('Tag', secondary=tags, lazy='subquery',
        backref=db.backref('pages', lazy=True))

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)

# test
# page = Page()
# tag = Tag()
# page.tags.append(tag)
# db.session.add(page)
# db.session.commit()

# page2 = Page()
# tag.append(page2)
# db.session.add(page2)
# db.session.commit()

# ---------------------------------------------------------------------

# One-to-Many
# class Person(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)
#     addresses = db.relationship('Address', backref='person', lazy=True)

# class Address(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(120), nullable=False)
#     person_id = db.Column(db.Integer, db.ForeignKey('person.id'),
#         nullable=False)

# test
# person = Person()
# person.name = 'Ian'
# address = Address()
# address.email = 'test@gmail.com'
# address.person = person
# db.session.add(person)
# db.session.commit()
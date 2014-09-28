"""
models.py

"""
from apps import db

#
# add User Model
#

class Article(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(255))
	content = db.Column(db.Text())
	author = db.Column(db.String(255))
	category = db.Column(db.String(255))
	like = db.Column(db.Integer, default=0)
	date_created = db.Column(db.DateTime())


class Comment(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	article_id = db.Column(db.Integer, db.ForeignKey('article.id'))
	article = db.relationship('Article', backref=db.backref('comments', cascade='all, delete-orphan', lazy='dynamic'))
	author = db.Column(db.String(255))
	email = db.Column(db.String(255))
	password = db.Column(db.String(255))
	content = db.Column(db.Text())
	like = db.Column(db.Integer, default=0)
	date_created = db.Column(db.DateTime())

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(255))
	password = db.Column(db.String(255))
	name = db.Column(db.String(255))
	join_date = db.Column(db.DateTime())

#
#background
#
class Background(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_back = db.Column(db.Integer, db.ForeignKey('user.id'))
	user = db.relationship('User', backref=db.backref('backgrounds', cascade='all, delete-orphan', lazy='dynamic'))
	image_key = db.Column(db.String(255))

class Cookies(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_cookie = db.Column(db.Integer, db.ForeignKey('user.id'))
	users = db.relationship('User', backref=db.backref('cookie', cascade='all, delete-orphan', lazy='dynamic'))
	block_url0 = db.Column(db.String(255))
	block_url1 = db.Column(db.String(255))
	block_url2 = db.Column(db.String(255))
	block_url3 = db.Column(db.String(255))
	block_url4 = db.Column(db.String(255))
	block_url5 = db.Column(db.String(255))
	block_url6 = db.Column(db.String(255))
	block_url7 = db.Column(db.String(255))
	block_url8 = db.Column(db.String(255))
	block_url9 = db.Column(db.String(255))
	block_url10 = db.Column(db.String(255))
	block_url11 = db.Column(db.String(255))
	block_url12 = db.Column(db.String(255))
	block_url13 = db.Column(db.String(255))
	block_url14 = db.Column(db.String(255))
	block_url15 = db.Column(db.String(255))
	block_url16 = db.Column(db.String(255))
	block_url17 = db.Column(db.String(255))
	block_url18 = db.Column(db.String(255))
	block_url19 = db.Column(db.String(255))
	block_url20 = db.Column(db.String(255))
	block_url21 = db.Column(db.String(255))
	block_url22 = db.Column(db.String(255))
	block_url23 = db.Column(db.String(255))
	block_url24 = db.Column(db.String(255))

	block_url_img0 = db.Column(db.String(255))
	block_url_img1 = db.Column(db.String(255))
	block_url_img2 = db.Column(db.String(255))
	block_url_img3 = db.Column(db.String(255))
	block_url_img4 = db.Column(db.String(255))
	block_url_img5 = db.Column(db.String(255))
	block_url_img6 = db.Column(db.String(255))
	block_url_img7 = db.Column(db.String(255))
	block_url_img8 = db.Column(db.String(255))
	block_url_img9 = db.Column(db.String(255))
	block_url_img10 = db.Column(db.String(255))
	block_url_img11 = db.Column(db.String(255))
	block_url_img12 = db.Column(db.String(255))
	block_url_img13 = db.Column(db.String(255))
	block_url_img14 = db.Column(db.String(255))
	block_url_img15 = db.Column(db.String(255))
	block_url_img16 = db.Column(db.String(255))
	block_url_img17 = db.Column(db.String(255))
	block_url_img18 = db.Column(db.String(255))
	block_url_img19 = db.Column(db.String(255))
	block_url_img20 = db.Column(db.String(255))
	block_url_img21 = db.Column(db.String(255))
	block_url_img22 = db.Column(db.String(255))
	block_url_img23 = db.Column(db.String(255))
	block_url_img24 = db.Column(db.String(255))

	block_widget0 = db.Column(db.String(255))
	block_widget1 = db.Column(db.String(255))
	block_widget2 = db.Column(db.String(255))
	block_widget3 = db.Column(db.String(255))
	block_widget4 = db.Column(db.String(255))
	block_widget5 = db.Column(db.String(255))
	block_widget6 = db.Column(db.String(255))
	block_widget7 = db.Column(db.String(255))
	block_widget8 = db.Column(db.String(255))
	block_widget9 = db.Column(db.String(255))
	block_widget10 = db.Column(db.String(255))
	block_widget11 = db.Column(db.String(255))
	block_widget12 = db.Column(db.String(255))
	block_widget13 = db.Column(db.String(255))
	block_widget14 = db.Column(db.String(255))
	block_widget15 = db.Column(db.String(255))
	block_widget16 = db.Column(db.String(255))
	block_widget17 = db.Column(db.String(255))
	block_widget18 = db.Column(db.String(255))
	block_widget19 = db.Column(db.String(255))
	block_widget20 = db.Column(db.String(255))
	block_widget21 = db.Column(db.String(255))
	block_widget22 = db.Column(db.String(255))
	block_widget23 = db.Column(db.String(255))
	block_widget24 = db.Column(db.String(255))

	division_col = db.Column(db.Integer)
	division_row = db.Column(db.Integer)
	search = db.Column(db.String(255))












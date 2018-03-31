from . import db


class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    gender = db.Column(db.String(1))
    email = db.Column(db.String(80), unique=True)
    location = db.Column(db.String(100))
    biography = db.Column(db.String(300))
    image_url = db.Column(db.String(150))
    created_on=db.Column(db.DateTime)

    def __init__(self,first_name,last_name,gender,email,location,biography,image_url,created_on):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.gender=gender
        self.location=location
        self.biography=biography
        self.image_url=image_url
        self.created_on=created_on
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)

from sqlalchemy.orm import defaultload
from basicm import *


class userpassdb(UserMixin, db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now)

    def get_id(self):
        return self.sno


class otpdb(db.Model):
    # myotp=str(randint(100000,999999))
    sno = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), default="None")
    email = db.Column(db.String(50), default="None")
    otp = db.Column(db.String(10), nullable=False)
    time = db.Column(db.DateTime, default=datetime.now)


class userInfodb(db.Model):
    pic = open("defaultprofile.jpg", 'rb')
    filename = secure_filename("defaultprofile.jpg")
    mimetype = "image/jpeg"

    sno = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)

    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)

    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(20))

    intro = db.Column(db.String(200), default="")

    gender = db.Column(db.String(100), )
    age = db.Column(db.String(5))

    locationCity = db.Column(db.String(50))
    locationState = db.Column(db.String(50))
    locationCountry = db.Column(db.String(50))

    latitude = db.Column(db.String(100))
    longitude = db.Column(db.String(100))
    distance = db.Column(db.String(100))
    facebook = db.Column(db.String(200), default="https://www.facebook.com/")
    instagram = db.Column(db.String(200), default="https://www.instagram.com/")

    img = db.Column(db.Text, default=pic.read())
    imgname = db.Column(db.Text, default=filename)
    imgmimetype = db.Column(db.Text, default=mimetype)

    membership = db.Column(db.String(50), default="Free")

    date_created = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.username} - {self.email} - {self.first_name} {self.last_name} "


class otherprofileImagesdb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    img = db.Column(db.Text)
    name = db.Column(db.Text)
    mimetype = db.Column(db.Text)
    date_created = db.Column(db.DateTime, default=datetime.now)


class chatsdb(db.Model):
    time = datetime.now()
    time = time.strftime("%m/%d/%Y, %H:%M:%S")

    id = db.Column(db.Integer, primary_key=True)
    
    fromuser = db.Column(db.String(50), nullable=False)
    touser = db.Column(db.String(50), nullable=False)
    chatmessage = db.Column(db.String(1000))

    chatimg = db.Column(db.Text)
    imagename = db.Column(db.Text)
    imagemimetype = db.Column(db.Text)

    altimglink = db.Column(db.Text)

    read = db.Column(db.String(50))
    deletemessageid = db.Column(db.String(50), default=False)
    chattime = db.Column(db.String(50), default=time)
    date_created = db.Column(db.DateTime, default=datetime.now)


class chatsuserdb(db.Model):
    time = datetime.now()
    time = time.strftime("%m/%d/%Y, %H:%M:%S")

    id = db.Column(db.Integer, primary_key=True)
    fromuser = db.Column(db.String(50), nullable=False)
    touser = db.Column(db.String(50), nullable=False)
    unreadt = db.Column(db.Integer, default=0)
    unreadf = db.Column(db.Integer, default=0)
    deletechatuserid = db.Column(db.String(50))
    lastmessage = db.Column(db.String(1000))
    chatusertime = db.Column(db.String(50), default=time)
    date_created = db.Column(db.DateTime, default=datetime.now)


class stickersdb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.Text, nullable=False)
    name = db.Column(db.Text, nullable=False)
    altimg = db.Column(db.Text)
    mimetype = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now)


class superLikedb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fromuser = db.Column(db.String(40))
    touser = db.Column(db.String(40))
    date_created = db.Column(db.DateTime, default=datetime.now)


class likedb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fromuser = db.Column(db.String(40))
    touser = db.Column(db.String(40))
    date_created = db.Column(db.DateTime, default=datetime.now)


class savedb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fromuser = db.Column(db.String(40))
    touser = db.Column(db.String(40))
    first_name = db.Column(db.String(40))
    last_name = db.Column(db.String(40))
    age = db.Column(db.String(40))
    city = db.Column(db.String(40))
    state = db.Column(db.String(40))
    date_created = db.Column(db.DateTime, default=datetime.now)


class sheduleDatesdb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fromuser = db.Column(db.String(40))
    touser = db.Column(db.String(40))
    name = db.Column(db.String(40))
    dtime = db.Column(db.String(50))
    ddate = db.Column(db.String(50))
    location = db.Column(db.String(100))
    latitude = db.Column(db.String(30))
    longitude = db.Column(db.String(30))
    date_created = db.Column(db.DateTime, default=datetime.now)


class notificationdb(db.Model):
    time = datetime.now()
    time = time.strftime("%m/%d/%Y, %H:%M:%S")

    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer, default=0)
    username = db.Column(db.String(40))
    text = db.Column(db.String(100))
    title = db.Column(db.String(100))
    type = db.Column(db.String(50))
    link = db.Column(db.String(100), default="#")
    ntime = db.Column(db.String(50), default=time)
    date_created = db.Column(db.DateTime, default=datetime.now)


class postsdb(db.Model):
    time = datetime.now()
    time = time.strftime("%m/%d/%Y, %H:%M:%S")

    id = db.Column(db.Integer, primary_key=True)
    like = db.Column(db.Integer, default=0)

    username = db.Column(db.String(40))
    name = db.Column(db.String(50))

    age = db.Column(db.String(100))

    City = db.Column(db.String(50))
    State = db.Column(db.String(50))
    Country = db.Column(db.String(50))
    latitude = db.Column(db.String(50))
    longitude = db.Column(db.String(50))
    img = db.Column(db.Text)
    imagename = db.Column(db.Text)
    imagemimetype = db.Column(db.Text)

    ntime = db.Column(db.String(50), default=time)
    date_created = db.Column(db.DateTime, default=datetime.now)


class postslikedb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    postid = db.Column(db.Integer)
    fusername = db.Column(db.String(40))
    date_created = db.Column(db.DateTime, default=datetime.now)


def addingmydata():
    pass

    # messageuser1=chatsuserdb(fromuser="user1",touser="user2",lastmessage="hi user how are you")
    # messageuser2=chatsuserdb(fromuser="user1",touser="user3",lastmessage="hi user how are you")
    # db.session.add(messageuser1)
    # db.session.add(messageuser2)
    # db.session.commit()

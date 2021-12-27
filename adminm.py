from sqlm import *
  
@app.route("/admin")
def admin():
    userpassm=userpassdb.query.all()
    userinfom=userInfodb.query.all()
    return render_template('Admin/admin.html', userpass=userpassm,userinfo=userinfom)




# adding database   
# adding database   
# adding database   
@app.route("/admin/addData",methods=[ "POST","GET"])
def adduserinfo():
    if request.method=="POST":
        username=request.form['username']
        first_name=request.form['firstname']
        lastname=request.form['lastname']
        phone=request.form['phone']
        email=request.form['email']
        intro=request.form['intro']
        gender=request.form['gender']
        age=request.form['age']
        dob=request.form['dob']
 
        userinfo = userInfodb(username=username,first_name=first_name,last_name=lastname,phone=phone,email=email,intro=intro,gender=gender,age=age,dob=dob)
        db.session.add(userinfo)
        db.session.commit()
        return "Added successfully"
    return render_template('Admin/databaseadd.html')

# adding database   
# adding database   
# adding database   




# admin stickers upload
# admin stickers upload


# show stickers
@app.route('/stickers/<int:id>')
def chatStickersImage(id):
    img = stickersdb.query.filter_by(id=id).first()
    if not img:
        return 'Img Not Found!', 404

    return Response(img.img, mimetype=img.mimetype)
# show stickers



@app.route('/admin/stickersul', methods=['POST', 'GET'])
def chatStickerUpload():
    if request.method == 'POST':
        pic = request.files['pic']
        if not pic:
            return 'No pic uploaded!', 400

        filename = secure_filename(pic.filename)
        mimetype = pic.mimetype
        if not filename or not mimetype:
            return 'Bad upload!', 400

        img = stickersdb(img=pic.read(), name=filename, mimetype=mimetype)
        db.session.add(img)
        db.session.commit()
        return 'Img Uploaded!', 200
    else:
        return render_template("Admin/stickersul.html")
# admin stickers upload
# admin stickers upload



#deleting database
#deleting database
#deleting database
@app.route("/admin/delete/userpass/<int:sno>")
def adminDeleteUserpass(sno):
    myTodo=userpassdb.query.filter_by(sno=sno).first()
    db.session.delete(myTodo)
    db.session.commit()
    return redirect("/admin")


@app.route("/admin/delete/userinfo/<int:sno>")
def adminDeleteUserinfo(sno):
    myTodo=userInfodb.query.filter_by(sno=sno).first()
    db.session.delete(myTodo)
    db.session.commit()
    return redirect("/admin")


#deleting database
#deleting database
#deleting database




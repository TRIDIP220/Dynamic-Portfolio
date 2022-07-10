from flask import Flask,render_template,request,session
import os
import uuid
#from flask_ngrok import run_with_ngrok


app = Flask(__name__)
#run_with_ngrok(app)
#app.secret_key = "SecretKey"

@app.route("/")
def home():
    return render_template("home.html")
@app.route("/design")

def design():
    return render_template("design.html")

@app.route("/form/<string:design>" ,methods = ["GET","POST"])
def form(design):
      session["design_sess"] = design
      return render_template("form.html")

@app.route("/d")
def d():
    return render_template("design1.html")


@app.route("/upload",methods=["GET" ,"POST"])
def upload():
    desging_upload = session.get("design_sess")
    if desging_upload == "design1":
        design_name ="Design1.html"

    elif desging_upload == "design2":
         design_name ="Design2.html"
    if request.method == 'POST':
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        odi= request.form.get('odi')
        one= request.form.get('one')
        bol = request.form.get('bol')
        college = request.form.get('college')
        phone = request.form.get('phone')
        email = request.form.get('email')
        skill1 = request.form.get('skill1')
        skill2 = request.form.get('skill2')
        skill3 = request.form.get('skill3')
        skill4 = request.form.get('skill4')
        about = request.form.get('about')
        localclub = request.form.get('localclub')
        state = request.form.get('state')
        role = request.form.get('role')
        wic = request.form.get('wic')
        bAB= request.form.get('bAB')
        boAB =request.form.get('boAB')
        key = uuid.uuid1()
        img = request.files["dp"]
        img_new_name = f"{key}{img.filename}"
        img.save(f"static/Image/{img.filename}")
        os.rename(f"static/Image/{img.filename}",f"static/Image/{img_new_name}")
      
      
      
        return render_template(design_name,dname = firstname,dlname = lastname,dODI =odi ,done=one,dbol = bol,img = img_new_name, dcol = college,dph = phone,demail = email,ds1 = skill1,ds2 = skill2,ds3 =skill3,ds4 = skill4,dabout = about,dlocal=localclub,dstate= state,drole=role,dwic=wic,dbattAB=bAB , dbowAB= boAB)

if __name__ == "__main__":
    #app.run(debug=True)
     app.run()
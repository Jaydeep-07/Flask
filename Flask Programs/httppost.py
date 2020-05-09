from flask import *  
app = Flask(__name__,template_folder='Template')  
  
@app.route('/loginpost',methods = ['POST'])  
def loginpost():  
      uname=request.form['uname']  
      passwrd=request.form['pass']  
      if uname=="jaydeep" and passwrd=="jd1234":  
          return "Welcome %s" %uname  
   
if __name__ == '__main__':  
   app.run(debug = True)  
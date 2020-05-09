from flask import *  
app = Flask(__name__,template_folder='Template')  
  
  
@app.route('/loginget',methods = ['GET'])  
def loginget():  
      uname=request.args.get('uname')  
      passwrd=request.args.get('pass')  
      if uname=="jaydeep" and passwrd=="jd1234":  
          return "Welcome %s" %uname  
   
if __name__ == '__main__':  
   app.run(debug = True)  
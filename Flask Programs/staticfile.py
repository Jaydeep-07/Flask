from flask import *  
app = Flask(__name__,template_folder='Template')  
 
@app.route('/')  
def message():  
      return render_template('message.html')  
if __name__ == '__main__':  
   app.run(debug = True)  
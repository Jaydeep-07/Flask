from flask import *  
app = Flask(__name__,template_folder='Template')  
  
@app.route('/table/<int:num>')  
def table(num):  
      return render_template('printtable.html',n=num)  
if __name__ == '__main__':  
   app.run(debug = True)
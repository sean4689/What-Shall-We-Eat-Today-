from flask import *
import findfood as fd
app = Flask(__name__)
@app.route("/",methods=['POST','GET'])
def go():
    if request.method=="POST":
        a=request.form['position']
        fdata=fd.finddata(3,str(a))
        # print(fdata)
        return render_template('index.html',fdata=fdata,ok="現在位置為:"+a)
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=1) 
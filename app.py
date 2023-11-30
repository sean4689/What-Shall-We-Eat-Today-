from flask import *
import findfood as fd
app = Flask(__name__)
@app.route("/",methods=['POST','GET'])
def go():
    if request.method=="POST":
        a=request.form['position']
        fdata=fd.finddata(1,str(a))
        fd.wwrite(fdata)
        a=fd.suffer()
        return render_template('index.html',key=a[0],img=a[1])
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=1) 
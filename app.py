from flask import *
import findfood as fd
app = Flask(__name__)
@app.route("/",methods=['POST','GET'])
def go():
    a=fd.suffer()
    return render_template('index.html',key=a[0],img=a[1])
if __name__ == '__main__':
    app.run(debug=1) 
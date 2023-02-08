from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi

ca = certifi.where(

)
client = MongoClient('mongodb+srv://test:sparta@cluster0.wlcw8cv.mongodb.net/luster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')
@app.route("/toyproject", methods=["POST"])
def toyproject_post():
    userid_receive = request.form["userid_give"]
    userpw_receive = request.form["userpw_give"]

    doc = {
        'userid': userid_receive,
        'userpw': userpw_receive
    }

    db.toyproject.insert_one(doc)
    return jsonify({'msg':'문제만들기!'})

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/test', methods=["GET"])
def toyproject_get():
    toyproject_list = list(db.toyproject.find({},{'_id':False}))
    return jsonify({'toyproject':toyproject_list})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)


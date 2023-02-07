from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@Cluster0.mhvqxjc.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/')
def home():
    return render_template('createQ.html')

@app.route('/create',methods=["POST"])
def save_post():
    num_receive = request.form['num_give']
    c_receive = request.form['c_give']

    print(num_receive, c_receive)

    doc = {
        'question_num':num_receive,
        'question_o':c_receive
    }
    db.toy.insert_one(doc)
    return jsonify({'msg':'답 저장 완료!'})

@app.route("/create", methods=["GET"])
def save_get():
    okay_list = list(db.toy.find({},{'_id':False}))
    return jsonify({'ok':okay_list})




if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@Cluster0.mhvqxjc.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/')
def home():
    return render_template('createQ.html')

@app.route('/create',methods=["POST"])
def save():
    question_receive = request.form['question_give']
    num_receive = request.form['num_give']
    question_name_receive = request.form['question_name_give']
    question1_receive = request.form['question1_give']
    question2_receive = request.form['question2_give']
    question3_receive = request.form['question3_give']
    question4_receive = request.form['question4_give']

    print(question_receive, num_receive, question_name_receive
          , question1_receive, question2_receive
          , question3_receive, question4_receive)

    doc = {
        'question':question_receive,
        'correctNum':num_receive,
        'question_name': question_name_receive,
        'question1':question1_receive,
        'question2': question2_receive,
        'question3': question3_receive,
        'question4': question4_receive,
    }
    db.toy.insert_one(doc)
    return jsonify({'msg':'답 저장 완료!'})






if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
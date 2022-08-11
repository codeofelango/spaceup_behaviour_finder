from flask import Flask , request , jsonify
import mysql.connector as conn
import pymongo


app = Flask(__name__)

@app.route('/mysqldata',methods=['GET','POST'])
def mysqldata():

    if(request.method == 'POST'):
        mydb = conn.connect(host='127.0.0.1', user='root', passwd='@Elango123')
        c = mydb.cursor()
        c.execute('use ineuron')
        mark = request.json['mark']
        print(mark)
        # mark = '22'
        print(mark)
        query = "select * from student where  marks > "+str(mark)
        print(query)
        data = c.execute(query)
        print(data)
        return jsonify(str(data))


@app.route('/mongodata',methods=['GET','POST'])
def mongodata():

    if(request.method == 'POST'):
        mark = request.json['mark']
        print(mark)
        client = pymongo.MongoClient(
            "mongodb+srv://mongodb:mongodb@cluster0.jdhc0.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        print('after password')
        db = client.test
        print('now here')
        print(db)
        collect = db["testcollect"]
        ngn =  collect.find({"q1":{"$not":{"$gte": mark}}})
        return jsonify(str(ngn))

if __name__ == '__main__':
    app.run(port=8000)

    

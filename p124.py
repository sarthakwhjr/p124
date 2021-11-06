from os import error
from flask import Flask,jsonify,request
app=Flask(__name__)
task=[
    {
        'id':1,
        'contact':u"123456789",
        'Name':u"Raju",
        'done':False
    

    },
    {
        'id':2,
        'contact':u"987654321",
        'Name':u"rahul",
        'done':False
    }
]
@app.route("/add-data",methods=["POST"])
def addtask():
    if(not request.json):
        return jsonify({
            'status':'error',
            'message':'please provide data'

        },400)
    task2={
        'id':task[-1]["id"]+1,
        'contact':request.json["contact"],
        'Name':request.json.get("Name",""),
        'done':False
    }
    task.append(task2)
    return jsonify({
        'status':'success',
        'message':'task added'


    })
@app.route("/get-data")
def gettask():
    return jsonify({
        'data':task

        })
if(__name__=="__main__"):
    app.run(debug=True)        
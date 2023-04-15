from flask import Flask, jsonify, request
# import requests
app = Flask(__name__)

tasks = [
    {
        "id": 1,
        "title": u'programming languages',
        "discription": u'c, c++, java, python',
        "done": False
    },
    {
        "id": 2,
        "title": u'IT companies ',
        "discription": u'cloudeq, tcs, hcl, nagaro, capgemini ',
        "done": False
    },

    {
        "id": 3,
        "title": u'Learn',
        "discription": u'AWS , Terraform , Python api',
        "done": False
    },
]


# @app.route('/')
@app.route('/doingFirstTime')
def hello_world():
    return 'Hello, World!'


@app.route('/Prefix', methods = ["Post"])
def add_task():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "Please provide the data"
        },400 )
    task = {

        "id": task[-1]['id'] + 1,
        "title": request.json['title'],
        "discription": request.json.get('discription', ""),
        "done": False
    }
    tasks.append(task)
    return jsonify ({

            "status": "success",
            "message": "Task added succesfuly"
         })

@app.route('/get-data')
def get_task():
    return jsonify({
        "data":tasks
    })

if __name__ == "__main__":
    app.run(debug=True)

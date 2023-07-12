from flask import Flask,render_template,request,jsonify

app = Flask(__name__)
#status format: <0 if not streaming, else URL>|<tokens earnt current session>|<time watched current session>|<tokens earnt all time>|<time watched all time>

current_status = "0|0|0|0|0|0"
errors = []

update = ""

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/connect/") #connects to data stream (we use long polling)
def connect():
    global update

    while update == "":
        pass


    text = update
    update = ""
    return jsonify({'text': text})

@app.route("/api/get_status/") #gets current status and errors
def get_status():
    return current_status + "|||" + "|".join(errors)

@app.route("/api/set_status/")
def set_status():
    status = request.headers.get("status")
    global current_status
    global update
    global errors
    current_status = status + "|2"


    update = "s|:|: " + current_status + "|||" + "|".join(errors)
    return "success!"

@app.route("/api/throw_error/")
def throw_error():
    error = request.headers.get("msg")
    global errors
    global current_status
    global update
    errors.append(error)

    update = "e|:|: " + error
    return "success!"

app.run(debug=True,use_reloader=False ,port=7676)
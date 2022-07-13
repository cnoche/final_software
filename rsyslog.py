from db import *
import sys

@app.route("/publisher", methods=['POST'])
def publish():
    message = request.form["message"]
    print(message, file=sys.stderr)
    topic = request.form["topic"]
    print(topic, file=sys.stderr)
    newMes = Message(message, topic)
    db.session.add(newMes)
    db.session.commit()

    return render_template("index.html")

@app.route("/subscriber/<topic>", methods=['GET'])
def subs(topic=None):
    for result in db.execute("SELECT * FROM Messages WHERE topic="+"'"+topic+"'"):
        print(result)
    return render_template("index.html")
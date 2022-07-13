from db import *
import sys

def create_app():
    app = Flask(__name__)
    return app
    
app = create_app()  

@app.route("/publisher", methods=['POST'])
def publish():
    message = request.form["message"]
    print(message, file=sys.stderr)
    topic = request.form["topic"]
    print(topic, file=sys.stderr)
    newMes = Message(message, topic)
    db.session.add(newMes)
    db.session.commit()

    return render_template("templates/index.html")

@app.route("/subscriber/<topic>", methods=['GET'])
def subs(topic=None):
    for result in db.engine.execute("SELECT * FROM Messages WHERE topic="+"'"+topic+"'"):
        print(result)
    return render_template("templates/index.html")

if __name__ == "__main__":
    app.run(debug=False)
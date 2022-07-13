import db
import sys

def create_app():
    app = db.Flask(__name__)
    return app
    
app = create_app()  

@app.route("/publisher", methods=['POST'])
def publish():
    message = db.request.form["message"]
    print(message, file=sys.stderr)
    topic = db.request.form["topic"]
    print(topic, file=sys.stderr)
    newMes = db.Message(message, topic)
    db.session.add(newMes)
    db.session.commit()

    return db.render_template("templates/index.html")

@app.route("/subscriber/<topic>", methods=['GET'])
def subs(topic=None):
    for result in db.engine.execute("SELECT * FROM Messages WHERE topic="+"'"+topic+"'"):
        print(result)
    return db.render_template("templates/index.html")

if __name__ == "__main__":
    app.run(debug=False)
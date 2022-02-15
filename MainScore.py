from flask import Flask


app = Flask(__name__)

@app.route("/MGC_GAMES")
def score_server():
    file = open("score.html")
    return file.read()

app.run(host='0.0.0.0' , port=4000, debug=True)


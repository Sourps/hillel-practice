from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route("/")

@app.route("/", methods = ['GET'])
def print_txt():
    path_txt = "/home/me/Desktop/Python/backups/hillel-practice/requirements/requirements.txt"
    if request.method == 'GET':
        f = open(path_txt, 'r')
        content = f.read()
    return render_template("book.html", content = content)

if __name__ == '__main__':
    app.run(debug=True)
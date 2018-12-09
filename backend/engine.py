import os
import sys
from flask import Flask, render_template, send_from_directory

from finder import KeywordFinder


app = Flask(__name__, template_folder='templates', static_folder='assets')


@app.route("/")
def home():
    return render_template('index.html')

@app.route('/assets/<path:folder>/<path:path>')
def send_assets(folder, path):
    print(app.static_folder, 'css', path)
    full_directory = os.path.join(app.static_folder, folder)
    print(full_directory)
    return send_from_directory(full_directory, path)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
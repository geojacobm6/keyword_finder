import os
import sys
from flask import Flask, render_template,\
    send_from_directory, request

from finder import KeywordFinder

global port

if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, '..', '..', 'templates')
    static_folder = os.path.join(sys._MEIPASS, '..', '..', 'assets')
    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
else:
    app = Flask(__name__, template_folder='../templates', static_folder='../assets')


@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        search = request.form['search']
        keyword_object = KeywordFinder()
        keyword_object.find_links(search)
        return render_template('index.html',
                               tags=keyword_object.TAG_DICT,
                               count=len(list(keyword_object.TAG_LIST)),
                               trending=keyword_object.CURRENT_TRENDING,
                               port=port)
    else:
        return render_template('starter.html', port=port)


@app.route('/assets/<path:folder>/<path:path>')
def send_assets(folder, path):
    full_directory = os.path.join(app.static_folder, folder)
    return send_from_directory(full_directory, path)


if __name__ == "__main__":
    port = sys.argv[1]
    app.run(host='0.0.0.0', port=port)

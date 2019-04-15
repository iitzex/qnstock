import os

import dropbox
from flask import Flask, render_template

from gen_html import generator

TOKEN = 'zKrtNUrN93AAAAAAAAAADdLM3ZHigfrm5bntL0vUR0pCXhKDWxGYaVIEsq8cLXRs'
dbx = dropbox.Dropbox(TOKEN)
app = Flask(__name__)


def get_file():
    dbx.files_download_to_file('links.csv', '/config/links.csv')
    dbx.files_download_to_file('tse.csv', '/config/tse.csv')
    dbx.files_download_to_file('filter.csv', '/config/filter.csv')


def main(name):
    get_file()
    generator(name)


@app.route('/')
def index():
    main('tse')

    return render_template('tse.html')


@app.route('/filter')
def filter():
    main('filter')

    return render_template('filter.html')


if __name__ == '__main__':
    debug = False
    if os.environ.get('PORT') is None:
        debug = True

    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=debug)

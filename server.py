import os

import dropbox

from flask import Flask, Markup, render_template

app = Flask(__name__)
TOKEN = 'zKrtNUrN93AAAAAAAAAADdLM3ZHigfrm5bntL0vUR0pCXhKDWxGYaVIEsq8cLXRs'
dbx = dropbox.Dropbox(TOKEN)


def get_file():
    dbx.files_download_to_file('templates/links.csv', '/config/links.csv')
    dbx.files_download_to_file('templates/tse.html', '/config/tse.html')
    dbx.files_download_to_file('templates/filter.html', '/config/filter.html')


@app.route('/')
def index():
    get_file()

    html = render_template('tse.html')
    return html


if __name__ == '__main__':
    debug = False
    if os.environ.get('PORT') is None:
        debug = True

    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=debug)

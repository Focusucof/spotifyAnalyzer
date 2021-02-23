from main import *

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def formRes():
    pl_id = request.form['playlist']
    getandsend(pl_id, offset)
    return render_template('result.html')

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r
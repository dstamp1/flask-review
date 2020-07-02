# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
import model as model
from dotenv import load_dotenv
load_dotenv()

# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        address = request.form['address']
        data = {}
        data['raw'] = model.google_civics_api(address)
        return render_template('results.html', data=data)
    else:
        return render_template('index.html',data={})
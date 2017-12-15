#!/usr/bin/env python3

##############################
# Author:  Albert Szadzinski #
# Date:    12.12.17          #
# Version: v0.2b             #
##############################

# import hyperdash
import time
from flask import Flask, render_template, flash, request, redirect, send_file, url_for

app = Flask(__name__)
app.secret_key = 'xD123'
app.debug = True
app.config['UPLOAD_FOLDER'] = 'data/raw/'
ALLOWED_EXTENSIONS = set(['png'])

###############################################

#_monitor = hyperdash.Experiment('Flask App')

################################################

types = ['Generate hologram',
         'Reconstruct image']

################################################

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/inline', methods=['POST', 'GET'])
def inline():
    if request.method == "POST":
        _type = request.form['type']
        _lambda = request.form['lambda']
        _distance = request.form['distance']
        _file = request.files['file']
        
        if _file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if _file and allowed_file(_file.filename):
            filename = str(int(time.time())) + '.png'
            _file.save(app.config['UPLOAD_FOLDER'] + filename)
        else:
            flash('Wrong extension')
            return redirect(request.url)
        '''
        return redirect(url_for('inline_result',
                                _type=_type,
                                _lambda=_lambda,
                                _distance=_distance))'''

    return render_template('inline.html', types=types)

@app.route('/inline/<_type><_lambda><_distance>')
def inline_result(_type, _lambda, _distance):
    return _type+_lambda

@app.route('/login', methods=['POST','GET'])
def login():
    return render_template('login.html')

#########################################################

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#########################################################

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

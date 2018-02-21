#!/usr/bin/env python3
##############################
# Author:  Albert Szadzinski #
# Date:    10.02.18          #
# Version: v1.1b             #
##############################


if __name__ == '__main__':
    import sys
    import time
    import Holopy.Webapp.hologen as hologen
    import Holopy.Webapp.config_app as config_app
    from flask import Flask, render_template, flash, request, redirect, send_file, url_for, session

    ######################### APP_config #####################
    sett = config_app.test(sys.argv)
    app = Flask(__name__)
    app.secret_key = 'holography'
    app.debug = True
    app.config['UPLOAD_FOLDER'] = sett['-d'] + 'Holopy_holo/raw/'
    ALLOWED_EXTENSIONS = set(['png'])



    ################# Global variables ######################

    img_path = 'static/Holopy_holo/'.format(sys.argv[0][:-11])
    holo_path = sett['-d'] + 'Holopy_holo/holo/'
    reholo_path = sett['-d'] + 'Holopy_holo/reholo/'
    types = ['Plane waves']

    ################### ROUTES ##############################

    @app.route('/')
    def home():
        return render_template('index.html')


    @app.route('/inline', methods=['POST', 'GET'])
    def inline():
        if request.method == "POST":
            session.clear()
            session['_type'] = request.form['type']
            session['_lambda'] = request.form['lambda']
            session['_distance'] = request.form['distance']
            session['res'] = request.form['resolution']
            _file = request.files['file']

            if _file.filename == '':
                flash('No selected file')
                return redirect(request.url)

            if _file and allowed_file(_file.filename):
                session['filename'] = str(int(time.time())) + '.png'
                _file.save(app.config['UPLOAD_FOLDER'] + session['filename'])
            else:
                flash('Wrong extension')
                return redirect(request.url)

            hologen.get_holo(app.config['UPLOAD_FOLDER'] + session['filename'],
                             holo_path + session['filename'],
                             reholo_path + session['filename'],
                             float(session['_distance']),
                             float(session['res']),
                             float(session['_lambda']) * 1e-9)

            return render_template('inline_result.html',
                                   types=types,
                                   _link=img_path + '/holo/' + session['filename'],
                                   _link2=img_path + '/reholo/' + session['filename'])

        return render_template('inline.html', types=types)


    @app.route('/login', methods=['POST', 'GET'])
    def login():
        return render_template('login.html')


    @app.route('/docs')
    def docs():
        return app.send_static_file('praca_inżynierska.pdf')


    #################### Functions ###########################

    def allowed_file(filename):
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


    ##########################################################

    app.run(host=sett['-i'], port=int(sett['-p']))

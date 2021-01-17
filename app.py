from flask import Flask, render_template, request, redirect, session, send_file
from werkzeug.utils import secure_filename
# import os

# Importing the libraries
# import numpy as np
# import matplotlib.pyplot as plt
import pandas as pd
# import seaborn as sns
# import pickle
# from flask.helpers import url_for
# from dask.dataframe.io import hdf

app = Flask(__name__)
app.secret_key = 'super_secret_key'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/analyze', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        if request.form['dataset'] == '':
            session['file_status'] = False
            return render_template('index.html', data='Please choose a dataset', success=False)
        else:
            lab_name = request.form['dataset']
            session['file_name'] = f'{lab_name}'
            session['file_status'] = True

            # Read the  file provides above, and assign it to variable "df"
            path = session['file_name']
            df = pd.read_csv(path, header=None)
            # print(path)
            
            exts = [".csv", ".json", ".xlsx", ".hdf"]
            
            for ext in exts:
                if session['file_name'].endswith(ext):
                    session['file_ext'] = ext

            if path == 'auto.csv':
                # create headers list
                headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style", "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight", "engine-type", "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio", "horsepower", "peak-rpm", "city-mpg", "highway-mpg", "price"]
                # # print("headers\n", headers)
                df.columns = headers

            return render_template('index.html', name=lab_name, head=df.describe(include="all").to_html())


@app.route('/head', methods=['GET', 'POST'])
def headers():
    # create headers list
    headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style", "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight", "engine-type", "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio", "horsepower", "peak-rpm", "city-mpg", "highway-mpg", "price"]
    
    if session['file_status']:
        # Read the  file provides above, and assign it to variable "df"
        if session['file_name'] == "auto.csv":
            path = 'auto.csv'
        elif session['file_name'] == "automobileEDA.csv":
            path = 'automobileEDA.csv'
        else:
            path = session['file_name']
            
        print(session['file_ext'])
               
        if session['file_ext'] == ".csv":
            df = pd.read_csv(path, header=None)
        elif session['file_ext'] == ".json":
            df = pd.read_json(path)
        elif session['file_ext'] == ".xlsx":
            df = pd.read_excel(path)
        elif session['file_ext'] == ".hdf":
            df = pd.read_hdf(path)
        
        if session['file_name'] == "auto.csv":
            df.columns = headers
        # # print("headers\n", headers)
    
        return render_template('index.html', name=path, data=df.head().to_html())
    else:
        return render_template('index.html', data='Please choose a dataset', success=False)


@app.route('/tail', methods=['GET', 'POST'])
def tail():
    # create headers list
    headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style", "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight", "engine-type", "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio", "horsepower", "peak-rpm", "city-mpg", "highway-mpg", "price"]
    
    if session['file_status']:
        # Read the  file provides above, and assign it to variable "df"
        if session['file_name'] == "auto.csv":
            path = 'auto.csv'
        elif session['file_name'] == "automobileEDA.csv":
            path = 'automobileEDA.csv'
        else:
            path = session['file_name']   
        if session['file_ext'] == ".csv":
            df = pd.read_csv(path, header=None)
        elif session['file_ext'] == ".json":
            df = pd.read_json(path)
        elif session['file_ext'] == ".xlsx":
            df = pd.read_excel(path)
        elif session['file_ext'] == ".hdf":
            df = pd.read_hdf(path)
        
        if session['file_name'] == "auto.csv":
            df.columns = headers
        # # print("headers\n", headers)
    
        return render_template('index.html', name=path, data=df.tail().to_html())
    else:
        return render_template('index.html', data='Please choose a dataset', success=False)


@app.route('/describe', methods=['GET', 'POST'])
def describe():
    # create headers list
    headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style", "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight", "engine-type", "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio", "horsepower", "peak-rpm", "city-mpg", "highway-mpg", "price"]
    
    if session['file_status']:
        # Read the  file provides above, and assign it to variable "df"
        if session['file_name'] == "auto.csv":
            path = 'auto.csv'
        elif session['file_name'] == "automobileEDA.csv":
            path = 'automobileEDA.csv'
        else:
            path = session['file_name']   
        if session['file_ext'] == ".csv":
            df = pd.read_csv(path, header=None)
        elif session['file_ext'] == ".json":
            df = pd.read_json(path)
        elif session['file_ext'] == ".xlsx":
            df = pd.read_excel(path)
        elif session['file_ext'] == ".hdf":
            df = pd.read_hdf(path)
        
        if session['file_name'] == "auto.csv":
            df.columns = headers
        # # print("headers\n", headers)
    
        return render_template('index.html', name=path, data=df.describe().to_html())
    else:
        return render_template('index.html', data='Please choose a dataset', success=False)


@app.route('/export', methods=['GET', 'POST'])
def export():
    if request.method == 'POST':
        formats = request.form['format']
        if session['file_status']:
            # create headers list
            headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style", "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight", "engine-type", "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio", "horsepower", "peak-rpm", "city-mpg", "highway-mpg", "price"]
        
            if formats == 'csv':
                    # Read the  file provides above, and assign it to variable "df"
                    if session['file_name'] == "auto.csv":
                        path = 'auto.csv'
                    elif session['file_name'] == "automobileEDA.csv":
                        path = 'automobileEDA.csv'
                    else:
                        path = session['file_name']  
                    df = pd.read_csv(path, header=None)
                    
                    if session['file_name'] == "auto.csv":
                        df.columns = headers
                    # # print("headers\n", headers)
                    df.to_csv('static/export/export.csv', index=False, encoding='utf-8-sig')
                    session['download'] = "export.csv"
                    return render_template('index.html', data='Successfully exported ' + session['file_name'] + ' to export.csv', success=True)
            elif formats == 'json':
                    # Read the  file provides above, and assign it to variable "df"
                    if session['file_name'] == "auto.csv":
                        path = 'auto.csv'
                    elif session['file_name'] == "automobileEDA.csv":
                        path = 'automobileEDA.csv'
                    else:
                        path = session['file_name']  
                    df = pd.read_csv(path, header=None)
                    
                    if session['file_name'] == "auto.csv":
                        df.columns = headers
                    # # print("headers\n", headers)
                    df.to_json("static/export/export.json")
                    session['download'] = "export.json"
                    return render_template('index.html', data='Successfully exported ' + session['file_name'] + ' to export.json', success=True)
            elif formats == 'excel':
                    # Read the  file provides above, and assign it to variable "df"
                    if session['file_name'] == "auto.csv":
                        path = 'auto.csv'
                    elif session['file_name'] == "automobileEDA.csv":
                        path = 'automobileEDA.csv'
                    else:
                        path = session['file_name']  
                    df = pd.read_csv(path, header=None)
                    
                    if session['file_name'] == "auto.csv":
                        df.columns = headers
                    # # print("headers\n", headers)
                    df.to_excel("static/export/export.xlsx", index=None)
                    session['download'] = "export.xlsx"
                    return render_template('index.html', data='Successfully exported ' + session['file_name'] + ' to export.xlsx', success=True)
            elif formats == 'hdf':
                    # Read the  file provides above, and assign it to variable "df"
                    if session['file_name'] == "auto.csv":
                        path = 'auto.csv'
                    elif session['file_name'] == "automobileEDA.csv":
                        path = 'automobileEDA.csv'
                    else:
                        path = session['file_name']  
                    df = pd.read_csv(path, header=None)
                    
                    if session['file_name'] == "auto.csv":
                        df.columns = headers
                    # # print("headers\n", headers)
                    df.to_hdf("static/export/export.hdf", mode="w", format="table", key="hdf")
                    session['download'] = "export.hdf"
                    return render_template('index.html', data='Successfully exported ' + session['file_name'] + ' to export.hdf', success=True)
        else:
            return render_template('index.html', data='Export failed! Please select or upload a dataset before export.', success=False)


@app.route('/run', methods=['GET', 'POST'])
def command():
    if request.method == 'POST':
        if request.form['custom-command'] == '':
            session['file_status'] = False
            return render_template('index.html', data='Please choose a dataset', success=False)
        else:
            lab_name = request.form['custom-command']
            session['file_name'] = f'{lab_name}'
            session['file_status'] = True

            # Read the  file provides above, and assign it to variable "df"
            path = f'{lab_name}'
            df = pd.read_csv(path, header=None)

            if f'{lab_name}' == 'auto.csv':
                # create headers list
                headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style", "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight", "engine-type", "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio", "horsepower", "peak-rpm", "city-mpg", "highway-mpg", "price"]
                # # print("headers\n", headers)
                df.columns = headers
            command = request.form['custom-command']
            # url = '/run/' + command
        return redirect('/run/' + command)


@app.route('/run/<string:command>', methods=['GET', 'POST'])
def run(command):
    if command == '':
        return render_template('index.html', data='Invalid command: ' + command, success=False)
    else:
        return render_template('index.html', data=exec(command).to_html())


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        
        exts = [".csv", ".json", ".xlsx", ".hdf"]
        
        if f:
            for ext in exts:
                if f.filename.endswith(ext):
                    f.save(secure_filename(f.filename))
                    session['file_name'] = f.filename
                    session['file_ext'] = ext
                    return redirect('/upload/' + f.filename)
            return render_template('index.html', data="Invalid file extension", success=False)
        else:
            return render_template('index.html', data="Upload failed. Please choose a file to upload", success=False)


@app.route('/upload/<file>', methods=['GET', 'POST'])
def fileUpload(file):
    if file:
        lab_name = file
        session['file_name'] = f'{lab_name}'
        session['file_status'] = True
    else:
        session['file_status'] = False
        return render_template('index.html', data='Please upload a file', success=False)

    # Read the  file provides above, and assign it to variable "df"
    path = f'{lab_name}'
    
    if session['file_ext'] == ".csv":
        df = pd.read_csv(path, header=None)
    elif session['file_ext'] == ".json":
        df = pd.read_json(path)
    elif session['file_ext'] == ".xlsx":
        df = pd.read_excel(path)
    elif session['file_ext'] == ".hdf":
        df = pd.read_hdf(path)
        
    return render_template('index.html', name=lab_name, head=df.describe(include="all").to_html())


@app.route('/download', methods=['GET', 'POST'])
def download():
    if session['file_name']:
        return send_file('static/export/' + session['download'], as_attachment=True)
    else:
        return render_template('index.html', data='Please choose a file to download', success=False)


@app.route('/reset')
def reset():
    session['file_name'] = ''
    session['file_status'] = False
    session['download'] = ''
    return render_template("index.html", data="Successfully reloaded!", success=True)


if __name__ == "__main__":
    app.run(debug=True)  # uncomment this when running on development mode i.e locally on your pc
    # app.run() #commet this when running on production mode i.e locally on your pc

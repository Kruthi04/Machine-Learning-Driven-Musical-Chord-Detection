from flask import Flask, render_template, request, redirect, url_for, session
# from pathlib import Path
# from tensorflow.keras.models import load_model
import numpy as np
# import cv2 as cv
import pandas as pd
import pickle as pkl
import librosa
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'raga'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = "Kurama@123"
app.config['MYSQL_DB'] = 'ragadetection'

mysql = MySQL(app)


dic = {0: 'asavari', 1: 'bageshree', 2 : "bhairavi", 3: 'bhoopali', 4: 'darbari', 5: 'dkanada', 6: 'malkauns', 7: 'sarangi', 8: 'yaman'}


# model = load_model('models/finalized_model_knn.sav')
# model = 'models/finalized_model_knn.sav'
rfc = pkl.load(open('models/RandomForestClassifier_model.pkl', 'rb'))


def predict_label(file):
    y, sr = librosa.load(file, mono=True, duration=30)
    chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
    rmse = librosa.feature.rms(y=y)
    spec_cent = librosa.feature.spectral_centroid(y=y, sr=sr)
    spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
    rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
    zcr = librosa.feature.zero_crossing_rate(y)
    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    to_append = f'{np.mean(chroma_stft)} {np.mean(rmse)} {np.mean(spec_cent)} {np.mean(spec_bw)} {np.mean(rolloff)} {np.mean(zcr)}'
    for e in mfcc:
        to_append += f' {np.mean(e)}'
    #         to_append += f' {g}'
    to_append = to_append.split()
    data = []
    data.append(to_append)

    result = rfc.predict(data)
    return dic[result[0]]


@app.route("/submit", methods=['GET', 'POST'])
def get_hours():
    if request.method == 'POST':
        file = request.files['audio']
        p = predict_label(file)
        return render_template("home.html", prediction=p)


user_mail = ''
user_name = ''


@app.route('/')
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form["email"]
        pwd = request.form["password"]
        cur = mysql.connection.cursor()
        cur.execute("select * from users where email=%s and password=%s", (email, pwd))
        user = cur.fetchone()
        if user:
            session['logged_in'] = True
            print(user)
            name = user[1]
            global user_mail
            user_mail = email
            global user_name
            user_name = name
            return render_template('home.html')
        else:
            msg = 'Invalid Login Details Try Again'
            return render_template('login.html', msg=msg, email=email)
    return render_template('login.html')


@app.route("/profile", methods=['GET', 'POST'])
def profile():
    mail = user_mail
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE email = %s ", [mail])
    data = cur.fetchone()
    username = data[3]
    # filename = username + '.jpg'
    # image = "static/register/" + filename
    print(data)
    return render_template("profile.html", data=data)


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        name = request.form.get('name',False)
        last_name = request.form.get('last_name',False)
        sex = request.form.get('gender',False)
        email = request.form.get('Email',False)
        city = request.form.get('city', False)
        country = request.form.get('country',False)
        Password = request.form.get('Password',False)
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT email FROM users WHERE email=%s", (email,))
        mail_user = cursor.fetchone()
        if not mail_user:
            cursor.execute('INSERT INTO users(name,last_name,gender,email,password,city,country)'
                           ' VALUES(%s,%s,%s,%s,%s,%s,%s)', (name, last_name, sex, email, Password, city, country))
            mysql.connection.commit()
            cursor.close()
            print("Records created successfully")

            if sex == 'Male':
                msg1 = " Hello mr." + name + " !! U Can login Here !!!"
                return render_template('login.html', msg=msg1, email=email)
            else:
                msg1 = " Hello ms." + name + " !! U Can login Here !!!"
                return render_template('login.html', msg=msg1, email=email)

        msg2 = "This Email Id is already Registered"
        return render_template('register.html', msg1=msg2)

    return render_template('register.html')


@app.route("/home", methods=['GET', 'POST'])
def home():
    return render_template("home.html")


@app.route('/password', methods=['POST', 'GET'])
def password():
    if request.method == 'POST':
        current_pass = request.form['current']
        new_pass = request.form['new']
        verify_pass = request.form['verify']
        email = user_mail[0]
        cur = mysql.connection.cursor()
        cur.execute("select password from users where email=%s", (email,))
        user = cur.fetchone()
        if user:
            print(user)
            if user == current_pass:
                if new_pass == verify_pass:
                    msg1 = 'Password changed successfully'
                    cur.execute("UPDATE users SET password = %s WHERE password=%s", (new_pass, current_pass))
                    mysql.connection.commit()
                    return render_template('password_change.html', msg1=msg1)
                else:
                    msg2 = 'Re-entered password is not matched'
                    return render_template('password_change.html', msg2=msg2)
            else:
                msg3 = 'Incorrect password'
                return render_template('password_change.html', msg3=msg3)
        else:
            msg3 = 'Incorrect password'
            return render_template('password_change.html', msg3=msg3)
    return render_template('password_change.html')


@app.route('/graphs', methods=['POST', 'GET'])
def graphs():
    return render_template('graphs.html')


@app.route('/logout')
def logout():
    session.clear()
    msg='You are now logged out', 'success'
    return redirect(url_for('login', msg=msg))


if __name__ == '__main__':
    app.run(debug=True)

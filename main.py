from flask import Flask, render_template, request, session, flash, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL
import os
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

app = Flask(__name__) #webserver
Bootstrap(app) #css framework

'''
Define Configuration for the MySQL pipeline
'''
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Indonesi13!!'
app.config['MYSQL_DB'] = 'dbPastiSampai'
# data get dict
app.config['MYSQL_CURSORCLASS'] = "DictCursor"

# make connection
mysql = MySQL(app)
# handling cookies transfering
app.config['SECRET_KEY'] = os.urandom(24)


# ------------------------------------------------------------------------
'''
Backend Setting of the CRUD App
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    cur = mysql.connection.cursor()
    result_value = cur.execute("SELECT * FROM tbstatusbarang")
    if result_value > 0:
        list = cur.fetchall()
    else:
        list = None
    return render_template('index.html', list=list)

@app.route('/inputData', methods=['GET', 'POST'])
def inputData():
    if request.method == 'POST':
        try:
            form = request.form
            id_pengiriman = form['id_pengiriman']
            tanggal_pengiriman = form['tanggal_pengiriman']
            jenis_pengiriman = form['jenis_pengiriman']
            jenis_barang = form['jenis_barang']
            asal_pengiriman = form['asal_pengiriman']
            tujuan_pengiriman = form['tujuan_pengiriman']
            status_pengiriman = form['status_pengiriman']
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO tbstatusbarang(id_pengiriman, tanggal_pengiriman, jenis_pengiriman, jenis_barang, asal_pengiriman, tujuan_pengiriman, status_pengiriman) VALUES(%s, %s, %s, %s, %s, %s, %s)", (id_pengiriman, tanggal_pengiriman, jenis_pengiriman, jenis_barang, asal_pengiriman, tujuan_pengiriman, status_pengiriman))
            mysql.connection.commit()
            flash('Successfully inserted data', 'success')
        except:
            flash('Failed to insert data', 'danger')
    return redirect(url_for('index'))

@app.route('/list')
def list():
    cur = mysql.connection.cursor()
    result_value = cur.execute("SELECT * FROM tbstatusbarang")
    if result_value > 0:
        list = cur.fetchall()
    return render_template('list.html', list=list)
    
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        try:
            form = request.form
            id_pengiriman = form['id_pengiriman']
            print(id_pengiriman)
            cur = mysql.connection.cursor()
            result_value = cur.execute("SELECT * FROM tbstatusbarang WHERE id_pengiriman = %s", (id_pengiriman,))
            if result_value > 0:
                list = cur.fetchall()
            return render_template('index.html', list=list)
            flah('Successfully searched data', 'success')
        except:
            flash('Failed to search data', 'danger')
    return redirect(url_for('index'))

@app.route('/update', methods=[ 'GET', 'POST'])
def update():
    if request.method == 'POST':
        try:
            id_pengiriman = request.form['id_pengiriman']
            tanggal_pengiriman = request.form['tanggal_pengiriman']
            jenis_pengiriman = request.form['jenis_pengiriman']
            jenis_barang = request.form['jenis_barang']
            asal_pengiriman = request.form['asal_pengiriman']
            tujuan_pengiriman = request.form['tujuan_pengiriman']
            status_pengiriman = request.form['status_pengiriman']
            cur = mysql.connection.cursor()
            result_value = cur.execute("UPDATE tbstatusbarang SET tanggal_pengiriman = %s, jenis_pengiriman = %s, jenis_barang = %s, asal_pengiriman = %s, tujuan_pengiriman = %s, status_pengiriman = %s WHERE id_pengiriman = %s", (tanggal_pengiriman, jenis_pengiriman, jenis_barang, asal_pengiriman, tujuan_pengiriman, status_pengiriman, id_pengiriman))
            mysql.connection.commit()
            flash('Successfully updated data', 'success')
        except:
            flash('Failed to update data', 'danger')
    return redirect(url_for('index'))

@app.route('/delete/<string:id_pengiriman>')
def delete(id_pengiriman):
    try:
        cur = mysql.connection.cursor()
        result_value = cur.execute("DELETE FROM tbstatusbarang WHERE id_pengiriman = %s", (id_pengiriman))
        mysql.connection.commit()
        flash('Successfully deleted data', 'success')
    except:
        flash('Failed to delete data', 'danger')
    return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(e):
    return 'This page was not found'

@app.route('/css')
def css():
    return render_template('css.html')

if __name__ == '__main__':
    app.run(debug=True) # also define a port app.run(debug=True, port=50001)
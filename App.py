from flask import Flask, render_template, request, redirect, url_for, flash

import pymysql



app = Flask(__name__)
app.secret_key = "flash message"






@app.route('/')
def Index():
    con = pymysql.connect(host="localhost", user="root", passwd="", db="crudapplication")
    cur = con.cursor()
    cur.execute("SELECT * FROM students")
    data = cur.fetchall()
    cur.close()

    return render_template('index.html', students = data)


@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == 'POST':
        flash("Data Inserted Successfully")

        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        con = pymysql.connect(host="localhost", user="root", passwd="", db="crudapplication")
        cur = con.cursor()
        cur.execute("INSERT INTO students (name, email, phone) VALUES (%s, %s, %s)", (name, email, phone))
        con.commit()
        return redirect(url_for('Index'))


@app.route('/update', methods=['POST', 'GET'])
def update():
    if request.method == 'POST':
        id_data = request.form['id']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        con = pymysql.connect(host="localhost", user="root", passwd="", db="crudapplication")
        cur = con.cursor()
        cur.execute("""
        UPDATE students
        SET name=%s, email=%s, phone=%s
        WHERE id=%s

        """, (name, email, phone, id_data))
        flash("Data Updated Successfully")
        con.commit()
        return redirect(url_for('Index'))


@app.route('/delete/<string:id_data>', methods=['POST', 'GET'])
def delete(id_data):
    con = pymysql.connect(host="localhost", user="root", passwd="", db="crudapplication")
    cur = con.cursor()
    cur.execute("DELETE FROM students WHERE id=%s", (id_data))
    flash("Data Deleted Successfully")
    con.commit()
    return redirect(url_for('Index'))




if __name__ == '__main__':
    app.run(debug=True)
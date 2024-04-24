from flask import Flask, url_for, render_template, current_app, g, request
from flaskext.mysql import MySQL

# creating a flask app
app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'drone_dispatch'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()
# cursor.execute("SHOW columns FROM drone_pilot_roster")
# print([column[0] for column in cursor.fetchall()])

# cursor.execute("SELECT * from User")
# data = cursor.fetchone()

@app.route("/", methods=['GET', 'POST'])
def main():
    return render_template('main.html')


@app.route("/views", methods=['GET', 'POST'])
def views():
    return render_template('views.html')

@app.route("/table/<name>")
def show_table(name):
    cursor.execute(f"SHOW columns FROM {name}")
    columns = [column[0] for column in cursor.fetchall()]
    cursor.execute(f"select * from {name}")
    rows = cursor.fetchall()

    return render_template('views.html', columns = columns, rows=rows)



if __name__ == "__main__":
    app.run()
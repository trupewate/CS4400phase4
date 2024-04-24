from flask import Flask, url_for, render_template, current_app, g, request
from flaskext.mysql import MySQL


## for reference
views = ["role_distribution", "customer_credit_check", "drone_pilot_roster", "drone_traffic_control"
         "store_sales_overview", "most_popular_products", "orders_in_progress"]
procedures = ["add_customer", "remove_customer", "add_product", "remove_product", "add_drone", "remove_drone",
              "add_drone_pilot", "swap_drone_control", "remove_drone_pilot",
              "repair_refuel_drone", "increase_customer_credits", "begin_order",
              "add_order_line", "deliver_order", "cancel_order"]

tables = ['customers', 'drone_pilots', 'drones', 'employed_workers', 'employees', 'order_lines', 
          'orders', 'products', 'store_workers', 'stores', 'users']
# creating a flask app
app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'kronoserj1418'
app.config['MYSQL_DATABASE_DB'] = 'drone_dispatch'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()
# cursor.execute("SHOW TABLES")
# print([table[0] for table in cursor.fetchall() if table[0] not in procedures and table[0] not in views])

# cursor.execute("SELECT * from User")
# data = cursor.fetchone()

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/tables')
def tables():
    return render_template('tables.html')

@app.route('/procedures')
def procedures():
    return render_template('procedures.html')

@app.route("/views")
def views():
    return render_template('views.html')

@app.route("/views/<name>")
def show_table(name):
    cursor.execute(f"SHOW columns FROM {name}")
    columns = [column[0] for column in cursor.fetchall()]
    cursor.execute(f"select * from {name}")
    rows = cursor.fetchall()

    return render_template('views.html', columns = columns, rows=rows)



if __name__ == "__main__":
    app.run()
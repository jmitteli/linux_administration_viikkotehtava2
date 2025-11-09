from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    # Yhdistetään MySQL/MariaDB:hen
    conn = mysql.connector.connect(
        host="localhost",
        user="exampleuser",
        password="change_this_strong_password",
        database="exampledb"
    )

    cursor = conn.cursor()

    # Haetaan MySQL-palvelimen kellonaika
    cursor.execute("SELECT NOW()")
    db_time = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    # Personoitu etusivu
    return f"""
    <html>
      <head>
        <title>LEMP-demo</title>
      </head>
      <body style="font-family: Arial; margin: 40px;">
        <h1>Tervetuloa Mikon LEMP-sivulle!</h1>
        <p>Tämä sivu pyörii Flask + Gunicorn + Nginx -kombolla.</p>
        <p><strong>MySQL-palvelimen kellonaika:</strong> {db_time}</p>
      </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

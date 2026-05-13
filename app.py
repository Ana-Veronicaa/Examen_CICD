from flask import Flask
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="database",
        user="root",
        password="rootpassword",
        database="Myapp_base",
        port=3306
    )

@app.route('/')
def hello():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT 'Hello from MySQL!' as message")
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return f"<h1>{result[0]}</h1><p>Aplicatie Flask + MySQL in Docker!</p>"
    except Exception as e:
        return f"<h1>Eroare: {str(e)}</h1>"

@app.route('/health')
def health():
    return {"status": "OK"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

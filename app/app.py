from flask import Flask, jsonify, Response
from pymongo import MongoClient
import mysql.connector
import os

app = Flask(__name__)

# MongoDB configuration
MONGO_HOST = os.getenv("MONGO_HOST", "mongo")
MONGO_PORT = int(os.getenv("MONGO_PORT", 27017))
MONGO_DB = os.getenv("MONGO_DB", "testdb")

# MySQL configuration
MYSQL_HOST = os.getenv("MYSQL_HOST", "mysql")
MYSQL_PORT = int(os.getenv("MYSQL_PORT", 3306))
MYSQL_USER = os.getenv("MYSQL_USER", "root")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "password")
MYSQL_DB = os.getenv("MYSQL_DB", "testdb")


@app.route('/test-devops', methods=['GET'])
def test_devops():
    """
    A simple test API for DevOps. Always returns HTTP 200.
    """
    return jsonify({"message": "DevOps test API is working fine"}), 200

@app.route('/simulate-error', methods=['GET'])
def simulate_error():
    """
    Simulates an error. Returns HTTP 502 if MongoDB is unreachable.
    """
    try:
        # Check MongoDB connectivity
        mongo_client = MongoClient(host=MONGO_HOST, port=MONGO_PORT, serverSelectionTimeoutMS=2000)
        mongo_client.server_info()  # Trigger server connection
        return jsonify({"message": "Everything is fine"}), 200
    except Exception as e:
        return jsonify({"error": "Simulated error: MongoDB is unreachable"}), 502

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

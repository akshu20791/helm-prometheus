from flask import Flask, request
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

# Custom metric: Count user logins
login_counter = Counter('user_logins_total', 'Number of user logins')

@app.route('/login', methods=['POST'])
def login():
    login_counter.inc()
    return "Login recorded", 200

@app.route('/metrics')
def metrics():
    return generate_latest(), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

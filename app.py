from flask import Flask, jsonify, render_template
from selenium_script import fetch_trending_topics
from store_in_mongodb import store_in_mongodb

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/run-script', methods=["GET"])
def run_script():
    proxy_ip = "XXX.XXX.XXX.XXX"  # Replace with actual proxy IP
    topics = fetch_trending_topics()
    result = store_in_mongodb(topics, proxy_ip)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)

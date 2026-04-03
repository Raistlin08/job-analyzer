from flask import Flask, send_file, jsonify, request

app = Flask(__name__)




@app.route('/')
def index():
    return send_file("templates/index.html")



@app.route('/analyze', methods=["POST"])
def analyze():
    data = request.get_json()
    print(data["job"])
    print(data["location"])
    return "sds"

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, send_file, jsonify, request

app = Flask(__name__)


standard_response = {
    "overview": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc rhoncus orci vel ante vehicula, ut sollicitudin tellus condimentum. Sed tortor velit, molestie ac tortor vel, tincidunt rutrum nunc. Duis egestas, mi sed tempus convallis, augue leo vestibulum tortor, in sagittis nulla velit at est. Sed cursus nulla odio, et lacinia.",
    "skills": [
        {"skill": "C++", "desc": "C++ linguaggio sndja saondsaodjsojadso sdoasdsna kjndsajndanasaass","relevance":1,"difficulty":3},
        {"skill": "docker","desc": "Docker è un sistema dsdsmdsk f ndsj fndns djsjsfnsd ni dsdsv hsuidhvsiv rf dhvsuiidc cad","relevance":2,"difficulty":4}
    ]
}


@app.route('/')
def index():
    return send_file("templates/index.html")



@app.route('/analyze', methods=["POST"])
def analyze():
    data = request.get_json()
    print(data["job"])
    print(data["location"])
    
    return jsonify(standard_response), 200

if __name__ == '__main__':
    app.run(debug=True)
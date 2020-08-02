from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/foo', methods=['POST'])
def foo():
    # return "Hello World!"
    data = request.get_json()
    print(data)
    return jsonify(data)


if __name__ == '__main__':
    app.run()

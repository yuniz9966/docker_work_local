# def greeting(name: str, age: int) -> str:
#     res = f"HI, I'M {name}! I'M {age} y.o"
#
#     return res
#
#
# if __name__ == "__main__":
#     res = greeting("O'gway", 325)
#
#     print(res)


from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/')
def greetings():
    return jsonify(
        {
            "message": "Greetings!"
        }
    ), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

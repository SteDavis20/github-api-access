from flask import Flask
# from flask_cors import CORS, cross_origin

app = Flask(__name__)
# CORS(app)

# localhost:5000/testing
@app.route("/testing")
def get_test_values():
    return {"test": ["Test1", "Test2"]}

# api is run on localhost:5000
if __name__ == "__main__":
    app.run(debug=True)

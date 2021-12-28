from flask import Flask

app = Flask(__name__)

# localhost:5000/testing
@app.route('/testing')
def get_test_values():
    return {"test": ["Test1", "Test2"]}


# api is run on localhost:5000
if __name__ == "__main__":
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=5000)

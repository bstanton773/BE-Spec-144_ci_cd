from flask import Flask


app = Flask(__name__)


# Create a route with the endpoint /
# Status 200 OK on GET, 405 on POST
# Should return "Welcome to the Flask App"
@app.route('/', methods=['GET'])
def index():
    print('Hello World')
    return "Welcome to the Flask App"



if __name__ == "__main__":
    app.run(debug=True)

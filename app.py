from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello SIRAJ AHMAD  ALHUMDULILLAH YOU DONE CICD ON AWS EC2   INSHALLAH !"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
### new line add for testing ###
### new line add for testing ###
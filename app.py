from flask import Flask
app = Flask(__name__)

@app.route("/")
def Home():
  return "6006021612166 Apiwat Charanai"


if __name__ == '__main__':
  app.debug = True
  app.run(host='0.0.0.0', port=80)

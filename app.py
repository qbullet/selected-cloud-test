from flask import Flask, render_template, jsonify
app = Flask(__name__)

@app.route('/')
def Home():
  return render_template('home.html') 

@app.route('/about-us')
def AboutUs():
  return render_template('about-us.html')  

@app.route('/product')
def GetProduct():
  return jsonify(productName = 'test product')

if __name__ == '__main__':
  app.debug = True
  app.run(host='0.0.0.0', port=3030)

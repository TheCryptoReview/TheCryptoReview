from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
# @app.route("/index.html")
def home():
  return render_template("dashboard.html")

# @app.route("/dashboard.html")
# def about():
#   return render_template("dashboard.html")
    
app.run(host='0.0.0.0', port=8080)
from application import app
from flask import render_template

@app.route("/")
@app.route("/index.html")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/contact")
@app.route("/contact.html")
def contact():
    return render_template('contact.html')

@app.route("/blog1")
@app.route("/blog1.html")
def blog1():
    return render_template('blog1.html')

@app.route("/blog2")
@app.route("/blog2.html")
def blog2():
    return render_template('blog2.html')

@app.route("/blog3")
@app.route("/blog3.html")
def blog3():
    return render_template('blog3.html')

@app.route("/blog4")
@app.route("/blog4.html")
def blog4():
    return render_template('blog4.html')

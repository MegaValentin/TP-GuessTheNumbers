from flask import Flask, render_template

app=Flask(__name__)
#primer ruta
@app.route('/')
def index():
    return render_template('index.html')



    
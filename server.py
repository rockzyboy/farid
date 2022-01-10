from flask import Flask, render_template, url_for, request 
import csv

app = Flask(__name__)
@app.route('/')
def server():
    return render_template('/index.html')
        


@app.route('/submit_form',methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data= request.form.to_dict()
    
        return render_template('/thankyou.html')
    else:
        return 'something went wrong'


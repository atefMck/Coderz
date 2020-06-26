#!/usr/bin/python3
"""
starts a Flask web application
"""
from flask import Flask, render_template, request
import json
app = Flask(__name__)


def signup(data):
    if not data:
        return False
    data.pop('signup')
    email = data['email']
    jsonDB = open('data.json', 'r')
    DBcheck = jsonDB.read()
    if email in DBcheck:
        jsonDB.close()
        return (False, 'This user is already registred')
    else:
        jsonDB = open('data.json', 'a+')
        jsonDB.write(" ,{}".format(json.dumps(data)))
        jsonDB.close()
        return ('success')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.form:
        data = request.form.to_dict()
        if "signup" in data:
            response = signup(data)
            return render_template(
                'index.html',
                response=response
            )
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

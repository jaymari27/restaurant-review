from __init__ import app
from flask import Flask, render_template


# Home page
@app.route('/')
def index():
    return render_template('form.html')
        

if __name__ == '__main__':
    app.run(debug=True)
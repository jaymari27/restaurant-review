from flask import Flask, render_template, request

app = Flask(__name__)

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# On Submit
@app.route('/submit', methods=['POST'])
def submit():
    # Making sure that the method is POST
    if request.method == 'POST':
        customer = request.form['customer']
        waiter = request.form['waiter']
        rating = request.form['rating']
        comments = request.form['comments']

        # Data validation
        customerEmpty = False
        waiterEmpty = False
        commentsEmpty = False
        
        if (customer == ""):
            customerEmpty = True
        if (waiter == ""):
            waiterEmpty = True
        if (comments == ""):
            commentsEmpty = True
        if (customerEmpty == True or waiterEmpty == True):
            return render_template('index.html', customerEmpty=customerEmpty,waiterEmpty=waiterEmpty, commentsEmpty=commentsEmpty)
        else:
            return render_template('success.html', commentsEmpty=commentsEmpty, customer=customer, waiter=waiter, comments=comments, rating=rating)

if __name__ == '__main__':
    app.run(debug=True)
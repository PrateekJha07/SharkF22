from flask import Flask,render_template

shark=Flask(__name__)
@shark.route('/')
def home():
    return render_template('home.html')

@shark.route('/')
def tables():
    return render_template('table.html')

@shark.route('/season1')
def season1():
    return render_template('season1.html')




if __name__ == '__main__':
    shark.run(debug=True)

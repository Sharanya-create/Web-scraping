from flask import Flask,render_template
app=Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')
@app.route("/showOnclick")
def showOnclick():
    return render_template('first.html')


if __name__ == '__main__':
    app.run(debug=True);

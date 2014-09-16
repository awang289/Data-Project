from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    inStream = open("data01.csv",'r')
    data = inStream.read()
    inStream.close()
    rows = data.split("\n")
    return render_template("data.html", info = rows)

if __name__=="__main__":
    app.debug=True
    app.run() 

    

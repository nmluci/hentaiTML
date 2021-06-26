from flask import Flask, render_template, request, url_for, redirect
from libs import hentai, utils

nh = hentai.Hentai()
app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "index.html", 
    )

@app.route("/hentai/id/<nukeid>")
def hentaiTML(nukeid):
    return render_template(
        "hentai.html",
        book = nh.getDoujin(int(nukeid))
    )

@app.route("/doujin", methods= ['POST', 'GET'])
def findDoujin():
    print(request)
    if request.method == 'POST':
        nuked = request.form['nukecode']
        return redirect(url_for('hentaiTML', nukeid=nuked))
    else:
        return render_template("hentai.html")

@app.route("/random")
def getRandomDoujin():
    sauce = nh.random()
    return redirect(url_for('hentaiTML', nukeid=sauce))

app.run(debug=True)


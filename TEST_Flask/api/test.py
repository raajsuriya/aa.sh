from flask import Flask, render_template
from vegs import *
from frts import *
from bots import *
from grns import *
from plts import *
from drys import *
from vags import *
from arbs import *

app=Flask(__name__)

@app.route("/") # ROOT TO BE FIXED
@app.route("/home")
def home():
	return render_template("home.html")

@app.route("/about")
def about():
	return render_template("about.html",title="about")

@app.route("/vegetables")
def vegetables():
	return render_template("vegetables.html",title="vegetables",vegs=vegs)

@app.route("/fruits")
def fruits():
	return render_template("fruits.html",title="fruits",frts=frts)

@app.route("/botanicals")
def botanicals():
	return render_template("botanicals.html",title="botanicals",bots=bots)

@app.route("/grains")
def grains():
	return render_template("grains.html",title="grains",grns=grns)

@app.route("/poultry")
def poultry():
	return render_template("poultry.html",title="poultry",plts=plts)

@app.route("/dairy")
def dairy():
	return render_template("dairy.html",title="dairy",drys=drys)

@app.route("/vegan")
def vegan():
	return render_template("vegan.html",title="vegan",vags=vags)

@app.route("/arbitrary")
def arbitrary():
	return render_template("arbitrary.html",title="arbitrary",arbs=arbs)

if __name__=="__main__":
	app.run(debug=True)
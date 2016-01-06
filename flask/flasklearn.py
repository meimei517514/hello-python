from flask import Flask,request,abort,redirect,render_template

app = Flask(__name__)
app.debug = True
app.config["SECRET_KEY"] = "hard to guess"

@app.route("/")
def first_page():
	header = request.headers.get("User-Agent")
	return render_template("index.html")

@app.route("/redirect")
def redirect_page():
	print "sorry,page not found"
	return redirect("https://www.baidu.com")

@app.route("/user/<name>")
def dynamic_page(name):
	print name
	if not name:
		abort(404)	
	return render_template("name.html",name=name)

@app.errorhandler(404)
def error_page_define(e):
	return "this is a define 404 page"




if __name__ == "__main__":
	app.run()

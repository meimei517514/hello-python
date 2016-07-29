from flask import Flask,request,abort,redirect,render_template,url_for

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

@app.route("/slash/")
def slash_page():
	print "this is slash page"
	return render_template("index.html")

@app.route("/noslash")
def noslash_page():
	return render_template("index.html")

@app.route("/user/<name>")
def dynamic_page(name):
	print name
	if not name:
		abort(404)
	print url_for("dynamic_page",name=name)
	return render_template("name.html",name=url_for("noslash_page"))

@app.errorhandler(404)
def error_page_define(e):
	return "this is a define 404 page"

@app.route("/login",methods=["GET","POST"])
def login():
	if request.method=="GET":
		return render_template("login.html")

	else:
		return "weclome %s,you password is %s,have a niceday"%(request.form["name"],request.form["password"])	


if __name__ == "__main__":
	app.run()

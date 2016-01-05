from flask import Flask,request,abort,redirect

app = Flask(__name__)
app.debug = True
app.config["SECRET_KEY"] = "hard to guess"

@app.route("/")
def first_page():
	header = request.headers.get("User-Agent")
	return "hello,flask,this is %s" %header

@app.route("/redirect")
def redirect_page():
	print "sorry,page not found"
	return redirect("https://www.baidu.com")

@app.route("/user/<name>")
def dynamic_page(name):
	user_name = load_user(name)
	if not name:
		abort(404)	
	return "hello,%s,young man" %name

@app.errorhandler(404)
def error_page_define(e):
	return "this is a define 404 page"


if __name__ == "__main__":
	app.run()

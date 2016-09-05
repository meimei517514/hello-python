from flask import Flask,request,abort,redirect,render_template,url_for
from basecode.xmlrefer import *
from basecode.xmldiff import *
#from basecode.xmlcheck import*
from git import *
import re

app = Flask(__name__)

app.config["SECRET_KEY"] = "hard to guess"
@app.route("/")
def first_page():
    return redirect("https://0.0.0.0:5000/xmldiff")


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
    else:
        return render_template("name.html",name=name)


@app.errorhandler(404)
def error_page_define(e):
    return "hail hydra!!"



@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template("login.html")

    else:
        return "weclome %s,you password is %s,have a niceday"%(request.form["account"],request.form["password"])	

@app.route("/float")
def folat():
    return render_template("float.html")

@app.route("/header")
def header():
    return render_template("header.html")

@app.route("/borderimage")
def borderimage():
    return render_template("borderimage.html")

@app.route("/script")
def script():
    return render_template("script.html")

@app.route("/transform")
def transform():
    return render_template("transform.html")

@app.route("/login2")
def login2():
    return render_template("login2.html")

@app.route("/jqsample")
def jqsample():
    return render_template("jqsample.html")

@app.route("/ajsample")
def ajsample():
    return render_template("ajsample.html")

@app.route("/ajpost")
def ajpost():	
    return "weclome %s,you password is %s,have a niceday"%(request.form["name"],request.form["password"])	

@app.route("/treeview")
def treeview():
    return render_template("treeview.html")

def login():
    if request.method=="GET":
        return render_template("login.html")

    else:
        return "weclome %s,you password is %s,have a niceday"%(request.form["account"],request.form["password"])	
    
@app.route("/xmlrefer",methods=["GET","POST"])
def xmlrefer():

    upgrade_info =request.values.get("upgrade")

    file_selected=request.values.get("file_name",xml_names[0]) 

    sheet_selected=request.values.get("sheet_name")

    sheet_namedict,sheet_data = get_sheetinfo(file_selected,sheet_selected,xml_paths,upgrade_info) 

    sheet_data=get_workbookdata(sheet_data,file_selected) 

    return render_template("xmlrefer.html",xml_names=xml_names,sheet_namedict=sheet_namedict,file_selected=file_selected,sheet_data=sheet_data)


@app.route("/xmldiff",methods=["GET","POST"])
def xmldiff():	
 
    upgrade_info = request.values.get("upgrade_info")

    author_name = request.values.get("author_name")

    branch_name = request.values.get("branch_name")

    branch_list = get_gitbranch(branch_name)

    hash_list,hash_info,author_name = get_gitinfo(upgrade_info,author_name,branch_name)

    selected_hash = request.values.get("selected_hash",hash_list[0])

    selected_file = request.values.get("selected_file")

    selected_sheet = request.values.get("selected_sheet")

    file_namelist,sheet_namelist,author,other_diff,maped_diff=get_gitdiff(selected_hash,selected_file,selected_sheet,hash_list)

    return render_template("xmldiff.html",branch_list=branch_list,file_namelist=file_namelist,sheet_namelist=sheet_namelist,hash_info=hash_info,author_name=author_name,author=author,other_diff=other_diff,maped_diff=maped_diff)



@app.route("/xmlfile",methods=["GET","POST"])
def xmlcheck():	
 

    selected_file = request.values.get("selected_file")

    selected_sheet = request.values.get("selected_sheet")

    selected_hash = request.values.get("selected_hash",hash_list[0])

    sheet_namelist,other_diff,maped_diff=get_changediff(selected_file,selected_sheet)

    return render_template("xmlcheck.html",file_namelist=file_namelist,sheet_namelist=sheet_namelist,other_diff=other_diff,maped_diff=maped_diff)





if __name__ == "__main__":
    app.run(threaded=True,host="100.84.74.126")
    

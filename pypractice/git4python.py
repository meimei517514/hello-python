from git import *

repo=Repo.init("~/mygithub/hello-python/.git")

log_detail=repo.git.log("-b","-1","--pretty",'--author=ma','--pretty=format:%an %cn %cd %H')

rint log_detail,str(log_detail)


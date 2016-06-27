############################################################################
#
#						Kellton Tech Sol. Lmt
#						270, Phase 2 
#						Udyog Vihar
#						Gurgaon (122001)
#						Haryana (India)
############################################################################
#						Author		: Himanshu Bansal & Mahesh Salaria
#						Description : views.py file is responsible for 
#									  functionality of all the Django app
#						
############################################################################
#						Predefined Libraries

from django.shortcuts import render
from github import Github
from git import Repo
import git
import os
from subprocess import call


#						Global Variables
username = ""
password = ''
#							Code

# function used to shoe the first login page to user
def loginpage(request):
	return render(request, 'Interface/login.html', {})

# function responsible for saving data to db 
# connection to github and show all repositiories
def login_entry(request):
	global username
	global password
	repo_list = []
	username =  request.POST['login_username']
	password =  request.POST['login_password']
	github_obj = Github(username, password)
	for repo in github_obj.get_user().get_repos():
		repo_list.append(repo.name)
	return render(request, 'Interface/index.html', {"repo_names" : repo_list})

# function used to show repository details in html page
def match_repo(request):
	repo_detail =  request.POST['repository_value']
	print (repo_detail)
	return render(request, 'Interface/show_repo.html', {"item" : repo_detail})

def clone_repo(request):
	path_folder =  request.POST['gitclone_deploy']
	repo_name =  request.POST['repo_name']
	git_url = "https://github.com/" + username + "/" + repo_name + ".git"
	if (os.path.exists(path_folder)) == True:
		print ("yes")
		os.system("cd /" + path_folder)
		os.system("git pull " + git_url)
	else:
		print ("No")
		os.system("sudo mkdir " + path_folder)
		os.system("cd /" + path_folder)
		os.system("git clone " + git_url) 
	return render(request, 'Interface/logout.html', {})
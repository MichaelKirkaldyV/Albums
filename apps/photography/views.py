# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
import bcrypt
from Tkinter import *
import tkMessageBox
import tkSimpleDialog


def home(request):
  return render(request, "photography/home.html")

def register_page(request):
	return render(request, "photography/register.html")

def register_process(request):
	errors = User.objects.validate_user(request.POST)

	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error)
		return redirect('/register')

	else:
		firstname = request.POST['firstname']
		lastname = request.POST['lastname']
		username = request.POST['username']
		password = request.POST['password']
		hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
		User.objects.create(username=username, password=hashed_pw)
		print "User created!"
		return redirect('/login')

def login_process(request):
	username = request.POST['username']
	password = request.POST['password']

	user = User.objects.filter(username=username)

	if len(user) > 0:
		this_password = bcrypt.checkpw(password.encode(), user[0].password.encode())
		if this_password:
			request.session['id'] = user[0].id
			return redirect('/login')
		else:
			message.error(request, "Incorrect username/password combination")
			return redirect('/')
	else:
		message.error(request, "User does not exist")
		return redirect('/')

def dashboard(request):
	return render(request, "photography/dashboard.html")

#Tkinter uses a GUI to take a input from the client via dialog box.
def createAlbum(request):
	window = Tk()
	answer = tkSimpleDialog.askstring("Input", "Please enter an album name.")
	if answer: 
		print "Album created", answer
		Album.objects.create(name=answer)
	window.mainloop()
	return redirect('/dashboard')

def add_album(request):
	errors = Album.objects.validate_album(request.POST)

	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error)
		return redirect('/login')

	else:
		alert("Please enter a name!")
		name = request.POST['name']
		Album.objects.create(name=name)
		print "Album created"
		return redirect('/login')

def add_photo(request):
	return
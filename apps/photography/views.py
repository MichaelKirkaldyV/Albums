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
		user = User.objects.get(username=username)
		request.session['id'] = user.id
		print "User created!"
		print "Username", username
		print "password", password
		return redirect('/')

def login_process(request):
	errors = User.objects.validate_user2(request.POST)

	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error)
		return redirect('/home')

	username = request.POST['username']
	password = request.POST['password']

	user = User.objects.filter(username=username)

	if len(user) > 0:
		this_password = bcrypt.checkpw(password.encode(), user[0].password.encode())
		if this_password:
			request.session['id'] = user[0].id
			print "Welcome"
			return redirect('/dashboard')
		else:
			messages.error(request, "Incorrect username/password combination")
			print "Error"
			return redirect('/')
	else:
		messages.error(request, "User does not exist")
		print "Error"
		return redirect('/')

def dashboard(request):
	context = {
		"user": User.objects.get(id=request.session['id']),
		"albums": Album.objects.filter(user=request.session['id'])
	}
	return render(request, "photography/dashboard.html", context)

#Tkinter uses a GUI to take a input from the client via dialog box.
def createAlbum(request):
	user = User.objects.get(id=request.session['id'])
	window = Tk()
	answer = tkSimpleDialog.askstring("Input", "Please enter an album name.")
	if answer: 
		album = Album.objects.create(name=answer, user=user)
		request.session['album_id'] = album.id
		print request.session['album_id']
		print "Album created", answer
	window.mainloop()
	return redirect('/dashboard')

def album_page(request, id):
	album = Album.objects.get(id=id)
	context = {
		"photos": Photo.objects.filter(album=album)
	}
	return render(request, "photography/album.html", context)


def add_photo(request):
	_photo = request.FILES['photo']
	album = Album.objects.get(id=request.session['album_id'])
	photo = Photo.objects.create(image=_photo, album=album)
	print "Photo added"
	return redirect('/dashboard')



# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
import bcrypt


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
		email = request.POST['email']
		hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
		User.objects.create(firstname=firstname, lastname=lastname, email=email, username=username, password=hashed_pw)
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
		return redirect('/')

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
	if 'id' not in request.session:
		return redirect('/')
	else:
		context = {
			"user": User.objects.get(id=request.session['id']),
			"albums": Album.objects.filter(user=request.session['id']),
			"photos": Photo.objects.filter(_user=request.session['id'])
		}
		return render(request, "photography/dashboard.html", context)

def delete_album(request, id):
	Album.objects.filter(id=id).delete()
	return redirect('/dashboard')

#Tkinter uses a GUI to take a input from the client via dialog box.
def createAlbum(request):
	print request.POST['answer']
	name = request.POST['answer']
	user = User.objects.get(id=request.session['id'])
	album = Album.objects.create(name=name, user=user)
	request.session['album_id'] = album.id
	print request.session['album_id']
	print "Album created"
	return redirect('/dashboard')

def album_page(request, id):
	if 'id' not in request.session:
		return redirect('/')
	else:
		album = Album.objects.get(id=id)
		context = {
			"photos": Photo.objects.filter(album=album),
			"album": Album.objects.get(id=id)
		}
		return render(request, "photography/album.html", context)


def add_photo(request, id):
	 _photo = request.FILES['photo']
	 album = Album.objects.get(id=id)
	 photo = Photo.objects.create(image=_photo, album=album)
	 print "Photo added"
	 return redirect('/album_page/' + id) 

def details(request, id):
	if 'id' not in request.session:
		return redirect('/')
	else:
		context = {
			"photo": Photo.objects.get(id=id)
		}
		return render(request, "photography/photoDetail.html", context)

def delete(request, id, album_id):
	photo = Photo.objects.get(id=id)
	photo.delete()
	return redirect('/album_page/' + album_id)

def logout(request, id):
	request.session.clear()
	return redirect('/')

def create_description(request, id):
	description = request.POST['description']
	user = User.objects.get(id=request.session['id'])
	photo = Photo.objects.get(id=id)
	photo.description = description
	photo.save()
	print "Description added"
	return redirect('/details/' + id)





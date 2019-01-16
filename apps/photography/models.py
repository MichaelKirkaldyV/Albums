# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class UserManager(models.Manager):
	def validate_user(request, postData):
		errors = {}

		#validate firstname
		if len(postData['firstname']) < 3:
			errors['firstname'] = "First name must be longer than 3 characters"

		#validate lastname
		if len(postData['lastname']) < 3:
			errors['lastname'] = "Last name must be longer than 3 characters"

		#Validate username
		if len(postData['username']) < 3:
			errors['username'] = "Username name must be longer than 3 characters"

		#Validate password
		if len(postData['password']) < 8:
			errors['password'] = "Password must be longer than 8 characters"

			if postData['password'] != postData['cnfrm_password']:
					errors['cnfrm_password'] = "Passwords do not match"

		return errors

	def validate_user2(request, postData):
		errors = {}

		if len(postData['username']) < 3 or len(postData['username']) == 0:
			errors['username'] = "Username must be longer than 3 characters, Username cannot be blank"

		if len(postData['password']) < 8:
			errors['password'] = "Password must be longer than 8 characters"

			if len(postData['password']) == 0: 
				errors['password'] = "Password field cannot be blank"

		return errors	

class AlbumManager(models.Manager):
	def validate_album(request, postData):
		errors = {}

		#validate name
		if len(postData['name']) < 3:
			errors['name'] = "Album name must be longer than 3 characters"

		return errors

class User(models.Model):
	firstname = models.CharField(max_length=50)
	lastname = models.CharField(max_length=50)
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()

class Album(models.Model):
	name = models.CharField(max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(User, related_name="created_albums")
	objects = AlbumManager()

class Photo(models.Model):
	misc_image = models.ImageField(upload_to="misc", blank=True)
	image = models.ImageField(upload_to="media", blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	album = models.ForeignKey(Album, related_name="added_photo")


	

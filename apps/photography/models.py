# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django_thumbs.db.models import ImageWithThumbsField
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

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

		#Validate email
		try:
			validate_email(postData['email'])
		except ValidationError:
			errors['email'] = "This is not a valid email address"
		else:
			if User.objects.filter(email=postData['email']):
				errors['email'] = "This email is already in use"

		#Validate password
		if len(postData['password']) < 8:
			errors['password'] = "Password must be longer than 8 characters"

			if postData['password'] != postData['cnfrm_password']:
					errors['cnfrm_password'] = "Passwords do not match"

		return errors

	def validate_user2(request, postData):
		errors = {}

		if len(postData['username']) < 3:
			errors['username'] = "Username must be longer than 3 characters"

		if len(postData['username']) == 0:
			errors['username'] = "Username cannot be blank"

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
	email = models.EmailField(max_length=20)
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
	image = ImageWithThumbsField(upload_to="media", blank=True, sizes=((125,125), (200,200)))
	description = models.CharField(max_length=150)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	album = models.ForeignKey(Album, related_name="added_photo", blank=True, null=True)
	_user = models.ForeignKey(User, related_name="misc_images", blank=True, null=True)


	

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from datetime import time 
from django.urls import reverse
import uuid


#User phone numbers object
class NumObject(models.Model):
	
	title= models.CharField(max_length=50)
	number= models.IntegerField()
	ident= models.IntegerField(blank=True, null=True)
	usersave= models.CharField(max_length=100, blank= True)


	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		super(NumObject,self).save(*args,**kwargs)

	def get_absolute_url(self):
		return reverse('posts:detail', kwargs={'id': self.id})







#incoming numbers model
class BlackList(models.Model):

	#TOP LEVEL FIELDS 
	numkey = models.ForeignKey(NumObject)
	bnum = models.IntegerField(null= True)
	blocked = models.BooleanField(default=False)
	



	BLOCKED_TIMES_BEGIN = (
		(time(0,0),'12 AM'),
		(time(1,0),'1 AM'),
		(time(2,0),'2 AM'),
		(time(3,0),'3 AM'),
		(time(4,0),'4 AM'),
		(time(5,0),'5 AM'),
		(time(6,0),'6 AM'),
		(time(7,0),'7 AM'),
		(time(8,0),'8 AM'),
		(time(9,0),'9 AM'),
		(time(10,0),'10 AM'),
		(time(11,0),'11 AM'),
		(time(12,0),'12 PM'),
		(time(13,0),'1 PM'),
		(time(14,0),'2 PM'),
		(time(15,0),'3 PM'),
		(time(16,0),'4 PM'),
		(time(17,0),'5 PM'),
		(time(18,0),'6 PM'),
		(time(19,0),'7 PM'),
		(time(20,0),'8 PM'),
		(time(21,0),'9 PM'),
		(time(22,0),'10 PM'),
		(time(23,0),'11 PM'),

		)

	BLOCKED_TIMES_END = (
		(time(0,0),'12 AM'),
		(time(1,0),'1 AM'),
		(time(2,0),'2 AM'),
		(time(3,0),'3 AM'),
		(time(4,0),'4 AM'),
		(time(5,0),'5 AM'),
		(time(6,0),'6 AM'),
		(time(7,0),'7 AM'),
		(time(8,0),'8 AM'),
		(time(9,0),'9 AM'),
		(time(10,0),'10 AM'),
		(time(11,0),'11 AM'),
		(time(12,0),'12 PM'),
		(time(13,0),'1 PM'),
		(time(14,0),'2 PM'),
		(time(15,0),'3 PM'),
		(time(16,0),'4 PM'),
		(time(17,0),'5 PM'),
		(time(18,0),'6 PM'),
		(time(19,0),'7 PM'),
		(time(20,0),'8 PM'),
		(time(21,0),'9 PM'),
		(time(22,0),'10 PM'),
		(time(23,0),'11 PM'),

		)

	# START/END TIME FOR EACH DAY
	sun_begin_time= models.TimeField(choices=BLOCKED_TIMES_BEGIN, null=True, blank=True)
	sun_end_time= models.TimeField(choices= BLOCKED_TIMES_END,null=True, blank=True)

	sun_begin_time= models.TimeField(choices=BLOCKED_TIMES_BEGIN, null=True, blank=True)
	sun_end_time= models.TimeField(choices= BLOCKED_TIMES_END,null=True, blank=True)

	mon_begin_time= models.TimeField(choices=BLOCKED_TIMES_BEGIN, null=True, blank=True)
	mon_end_time= models.TimeField(choices= BLOCKED_TIMES_END,null=True, blank=True)

	tue_begin_time= models.TimeField(choices=BLOCKED_TIMES_BEGIN, null=True, blank=True)
	tue_end_time= models.TimeField(choices= BLOCKED_TIMES_END,null=True, blank=True)

	wed_begin_time= models.TimeField(choices=BLOCKED_TIMES_BEGIN, null=True, blank=True)
	wed_end_time= models.TimeField(choices= BLOCKED_TIMES_END,null=True, blank=True)

	thu_begin_time= models.TimeField(choices=BLOCKED_TIMES_BEGIN, null=True, blank=True)
	thu_end_time= models.TimeField(choices= BLOCKED_TIMES_END,null=True, blank=True)

	fri_begin_time= models.TimeField(choices=BLOCKED_TIMES_BEGIN, null=True, blank=True)
	fri_end_time= models.TimeField(choices= BLOCKED_TIMES_END,null=True, blank=True)

	sat_begin_time= models.TimeField(choices=BLOCKED_TIMES_BEGIN, null=True, blank=True)
	sat_end_time= models.TimeField(choices= BLOCKED_TIMES_END,null=True, blank=True)

	# DAYS CHECKED
	sun = models.BooleanField(default=False)
	mon = models.BooleanField(default=False)
	tue = models.BooleanField(default=False)
	wed = models.BooleanField(default=False)
	thu = models.BooleanField(default=False)
	fri = models.BooleanField(default=False)
	sat = models.BooleanField(default=False)


	# sound = models.OneToOneField()
	def get_absolute_url(self):
		return reverse('posts:detail', kwargs={'id':self.numkey.id})

#sounds object
class Sounds(models.Model):
	numobj = models.ForeignKey(NumObject)
	title = models.CharField(max_length=50)
	sound = models.FileField()
	unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('posts:sound_detail', kwargs={'pk':self.title.pk}  )

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView
from django.urls import reverse
from django.core.urlresolvers import reverse_lazy

from .models import NumObject, Sounds, BlackList
from .forms import PostForm, NumForm, BlacklistForm, AddRules, UpdateAudio

import json



#main wall displaying all USER numbers
@login_required
def index(request):
	
	listboy= NumObject.objects.all()
	instance= Sounds.objects.all()
	
	context= {
		'object_listboy': listboy,
		'instance':instance,
				
	}
	return render(request, 'wall.html', context)

#USER number detail 
@login_required
def post_detail(request,id= None):
	instance= get_object_or_404(NumObject, id=id)
	incomingform= BlacklistForm(request.POST or None, request.FILES or None)
	

	if incomingform.is_valid():
		instanceIncoming = incomingform.save(commit=False)
		instanceIncoming.save()
			
	context= {

		'incomingform': incomingform,
		# 'form' :incomingform,
		'title': instance.number,
		'instance': instance,
		'numkey': instance.title,
		
	}
	return render(request,'post_detail.html',context)

@login_required
def sound_detail(request,id= None):
	instance= get_object_or_404(Sounds, id=id)
	form= PostForm(request.POST or None, request.FILES or None)
	
	context= {		
		'instance': instance,
		'form':form,
	}
	return render(request,'sound_detail.html',context)


#SOUND UPLOAD VIEW
@login_required
def post_create(request):
	form= PostForm(request.POST or None, request.FILES or None)


	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect('/')
	context= {
		'form': form,
	}
	return render(request, 'post_form.html',context,)


#CREATE NEW AUDIO UPLOAD FROM BLOB
def post_create_new(request):
	form= PostForm(request.POST or None, request.FILES or None)


	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()		
		
	else:
		errors = form.errors
		return HttpResponse(simplejson.dumps(errors))
		
		
	return render(request, 'sound_detail.html')




#CREATE USER NUMBERS VIEW
@login_required
def post_createnum(request):
	form= NumForm(request.POST or None, request.FILES or None)


	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect('/')
	
	context= {
		'form': form,
	}
	return render(request, 'num_form.html',context)



#DELETE SOUND VIEW
def post_delete(request, id=id):
	sound= get_object_or_404(Sounds, id=id).delete()
	
	return redirect('posts:list')


#AJAX MIXIN
class AjaxableResponseMixin(object):
	def render_to_json_response(self, context, **response_kwargs):
		data = json.dumps(context)
		response_kwargs['content_type'] = 'application/json'
		return HttpResponse(data, **response_kwargs)

	def form_invalid(self, form):
		response = super(AjaxableResponseMixin, self).form_invalid(form)
		if self.request.is_ajax():
			return self.render_to_json_response(form.errors, status=400)
		else:
			return response

		def form_valid(self, form):
			response = super(AjaxableResponseMixin, self).form_valid(form)
		if self.request.is_ajax():
			data = {
			'pk': self.object.pk,
			}
			return self.render_to_json_response(data)
		else:
			return response




#UPDATE VIEW

class UpdateRules(AjaxableResponseMixin, UpdateView):
	model = BlackList
	form_class = AddRules	
	template_name= 'blacklist_form.html'
	# success_url = reverse_lazy('posts:list')

class UpdateSound(AjaxableResponseMixin, UpdateView):
	model = Sounds
	form_class = PostForm	
	template_name= 'update_sound.html'
	# success_url = reverse_lazy('/')






			

	
	



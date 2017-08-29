from django import forms
from .models import NumObject, Sounds, BlackList
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError

from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


import os

#form for sound upload
class PostForm(forms.ModelForm):

	# def clean_sound(self):
	# 	file = self.cleaned_data.get('sound',False)
		# mime = magic.from_buffer(file.read(), mime=True)
		# print(mime)
		# if not mime == 'audio/mpeg':
		# 	raise forms.ValidationError('File must be mp3')
		# else:
		# 	return file

		
		# if file:
		# 	if file.size > 4*1024*1024:
		# 		raise ValidationError("Audio file too large ( > 4mb )")
		# 	if not file.content_type in ["audio/mpeg","audio/mp3", "audio/mp4", "audio/ogg", "audio/wav", "audio/x-wav"]:
		# 		raise ValidationError("Wrong file type, make sure to use mp3/wav/mp4/ogg")
		# 	if not os.path.splitext(file.name)[1] in [".mp3",".mp4", ".m4a", ".oga", ".ogg", ".wav"]:
		# 		raise ValidationError("Doesn't have proper extension")
			
			
		# 	return file
		# else:
		# 	raise ValidationError("Couldn't read uploaded file")


	class Meta:
		model = Sounds

		fields = [
		'title',
		'numobj',
		'sound',
		]




class AjaxableResponseMixin(object):
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)
        else:
            return response


# class UpdateAudio(AjaxableResponseMixin, CreateView):
# 	class Meta:
# 		model = Sounds

# 		fields = [
# 		'sound',
# 		]


class UpdateAudio(forms.ModelForm):
	class Meta:
		model = Sounds

		fields = [
		'title',
		'sound',
		]



#form for the users's numbers
class NumForm(forms.ModelForm):

	class Meta:
		model = NumObject
		exclude = ["user"]
		fields = [
		'title',
		'number',
		
		'usersave',
					
		]

#form for the incoming numbers
class BlacklistForm(forms.ModelForm):
	prefix = 'incomingnum'

	class Meta:
		model = BlackList
		fields = [
		'numkey',
		'bnum',
					
		]

#form for adding rules to incoming numbers
class AddRules(forms.ModelForm):
	prefix = 'rules'
	class Meta:
		model = BlackList
		exclude = ["numkey"]
		fields = [

		'numkey',
		'bnum',
		'sun',
		'mon',
		'tue',
		'wed',
		'thu',
		'fri',
		'sat',
		'blocked',
		'sun_begin_time',
		'sun_end_time',
		'mon_begin_time',
		'mon_end_time',
		'tue_begin_time',
		'tue_end_time',
		'wed_begin_time',
		'wed_end_time',
		'thu_begin_time',
		'thu_end_time',
		'fri_begin_time',
		'fri_end_time',
		'sat_begin_time',
		'sat_end_time',
		

		]





























		





























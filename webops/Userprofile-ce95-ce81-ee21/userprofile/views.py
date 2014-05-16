# Create your views here.
from django.shortcuts import render_to_response
from userprofile.models import Userprofile
from django.template import RequestContext, loader
from django.conf import settings
from django.contrib.auth.models import User
  
def userprofiles(request,user_id):
  a = Userprofile.objects.get(id=user_id)
  return render_to_response("index.html",locals(),context_instance=RequestContext(request))

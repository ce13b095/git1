from django.db import models

# Create your models here.

class Userprofile(models.Model):
  user_id =         models.CharField(max_length=4)
  first_name =      models.CharField(max_length=20)
  last_name =       models.CharField(max_length=20)
  email =           models.EmailField()
  no_projects =     models.CharField(max_length=5)
  points_earned =   models.CharField(max_length=10)
  skills  =         models.CharField(max_length=20)
  no_sessions =     models.CharField(max_length=3)
  image =           models.ImageField(upload_to='images')
  
  def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

  
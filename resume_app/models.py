from django.db import models

# Create your models here.
class Profile(models.Model):
   
	name = models.CharField(max_length=50,null=True,blank=True)
	email=models.EmailField(max_length=254,null=True,blank=True)
	skills = models.CharField(max_length=50,null=True,blank=True)
	semester = models.CharField(max_length=50,null=True,blank=True)
	image = models.ImageField(upload_to="images",null=True,blank=True)
   
	
	
	def save(self,*args, **kwargs):
		super().save(self,*args, **kwargs)
		
		
   
	@property
	def imageUrl(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url
	
  
   
	
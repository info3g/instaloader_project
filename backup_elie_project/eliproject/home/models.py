from django.db import models



class groupa_users(models.Model):
	username = models.CharField(max_length = 100, blank=True, null=True) 
	groupb_followers = models.TextField(blank=True, null=True) 

class groupb_users(models.Model):
	username = models.CharField(max_length = 100, blank=True, null=True) 
	groupa_followers = models.TextField(blank=True, null=True) 

class groupA_all_users(models.Model):
	username = models.CharField(max_length = 100, blank=True, null=True) 

	def __str__(self):
  		return self.username

class groupB_all_users(models.Model):
	username = models.CharField(max_length = 100, blank=True, null=True) 
	def __str__(self):
  		return self.username
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class user_profile(models.Model):
	user_name = models.CharField(max_length=200)
	user_email = models.CharField(max_length=200)
	user_phone = models.IntegerField(max_length=10)


class list_item(models.Model):
	profile = models.ForeignKey(user_profile, on_delete=models.CASCADE)
	todo_text = models.CharField(max_length=500)
	item = models.ForeignKey('self', null=True, default=None)
	children = models.ManyToManyField('self', null=True, blank=True)
	sequence_no = models.IntegerField(max_length=3, )
	def __str__(self):
		return self.todo_text
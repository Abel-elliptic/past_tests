from django.db import models
import uuid

class University(models.Model):
	# 大学情報、大学名と学部名情報が含まれる
	name = models.CharField("大学名", max_length=31)
	department = models.CharField("学部名", max_length=31)
	def __str__(self):
		return self.name + " " + self.department

class Univ_detail(models.Model):
	# 学科情報、学科名と学年情報が含まれる
	department_name = models.CharField("学部名", max_length=31)
	subject_name = models.CharField("学科名", max_length=31)
	school_year = models.IntegerField("学年")
	uuid = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
	def __str__(self):
		return self.department_name + " " + self.subject_name + " " + str(self.school_year) + "年生"

class Category(models.Model):
	univ = models.CharField("大学名", max_length=31)
	parent = models.CharField("親", max_length=31, blank=True)
	child = models.CharField("子", max_length=31)
	def __str__(self):
		if not self.parent:
			return self.child + "大学"
		elif self.univ == self.parent:
			return self.parent + "大学" + self.child
		else:
			return self.univ + "大学" + self.parent + self.child
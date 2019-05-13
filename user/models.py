from django.db import models

class Account(models.Model):
	# ユーザー情報
	first_name = models.CharField("性", max_length=31)
	last_name = models.CharField("名", max_length=31)
	mail_address = models.CharField("メール", max_length=31)
	telephone_number = models.CharField("電話番号", max_length=31)
	password = models.CharField("パスワード", max_length=63)
	university = models.CharField("大学名", max_length=31)
	department = models.CharField("学部名", max_length=31)
	subject = models.CharField("学科名", max_length=31)
	school_year = models.CharField("学年", max_length=31)
	def __str__(self):
		return self.first_name + self.last_name
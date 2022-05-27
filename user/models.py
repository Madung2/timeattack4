#user/models.py
from django.db import models


# Create your models here.
class UserClass(models.Model):
    class Meta:
        db_table = "my_user"

    def __init__(self,email,password):
        """회원가입 속성 초기화"""
        self.email = email
        self.password = password

 


# # Create your models here.
# class UserClass(models.Model):
#     class Meta:
#         db_table = "my_user"
#
#     email = models.CharField(max_length=20, null=False)
#     password = models.CharField(max_length=256, null=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
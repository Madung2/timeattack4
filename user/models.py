#user/models.py
from django.db import models


# Create your models here.
class UserClass(models.Model):
    class Meta:
        db_table = "my_user"

    def __init__(self, email, password):
        """회원가입 속성 초기화"""

        self.email = models.CharField(max_length=20, null=False)
        self.password = models.CharField(max_length=256, null=False)
        self.created_at = models.DateTimeField(auto_now_add=True)
        self.updated_at = models.DateTimeField(auto_now=True)





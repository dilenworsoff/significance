from django.db import models
from django.contrib.auth.models import User

# user
# test completed at time
# number of visitors, number of conversions
# variant number of visitors, and variant conversions
# winner

class Test(models.Model):
    title = models.CharField(max_length=150, default="")
    a_users = models.IntegerField(default=0)
    a_conversions = models.IntegerField(default=0)
    a_conversionrate = models.IntegerField(default=0)
    b_users = models.IntegerField(default=0)
    b_conversions = models.IntegerField(default=0)
    b_conversionrate = models.IntegerField(default=0)
    winner = models.CharField(max_length=150, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, default=0)

    def get_conv():
        a = a_users
        b = b_users
        return "HELLO"

    def __str__(self):
        return self.title

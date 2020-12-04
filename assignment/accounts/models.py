from django.db import models
from django.contrib.auth.models import User

DISTRICT_CHOICE = [
    ('' , '--------') ,('Purchase Manager' , 'Purchase Manager') , ('District Manager' , 'District Manager')
]
CITY_CHOICE =[
    ('' , '--------') , ('Aizawl' , 'Aizawl') ,('Lunglei' , 'Lunglei')
]


class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    designation = models.CharField(choices=DISTRICT_CHOICE , max_length=20)
    city = models.CharField(choices=CITY_CHOICE , max_length=20)
    join = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

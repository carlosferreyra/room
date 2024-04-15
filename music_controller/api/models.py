from django.db import models
import string, random
# Create your models here. (Fat Models, thin Views)
def generate_unique_code():
    # create a unique code for each room
    length = 6
    while True:
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
        if not Room.objects.filter(code=code).exists():
            break
    return code


class Room(models.Model):
    code = models.CharField(max_length=8,default='', unique=True)
    host = models.CharField(max_length=50,default='',unique=True)
    guest_can_pause = models.BooleanField(null=False,default=False)
    votes_to_skip = models.IntegerField(null=False,default=1)
    created_at = models.DateTimeField(auto_now_add=True)
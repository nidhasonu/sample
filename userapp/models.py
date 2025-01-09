from django.db import models
from django.contrib.auth.models import AbstractUser,  Group, Permission
import random,string,json
# Create your models here.



class Usermodel(AbstractUser):

    user_profile = [
        ('ADMIN', 'admin'),
        ('STUDENT', 'student'),
        ('COLLEGE', 'college'),

    ]

    user_type = models.CharField(max_length=20, choices=user_profile,null=True,blank=True)
    status = models.CharField(default="pending", max_length=20, null=True, blank=True, choices=[
            ('pending', 'Pending'),
            ('verified', 'Verified'),
            ('rejected', 'Rejected'),
        ])

    is_active = models.BooleanField(default=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    groups = models.ManyToManyField(Group, related_name="userapp_usermodel_groups")
    user_permissions = models.ManyToManyField(Permission, related_name="userapp_usermodel_permissions")

class Token(models.Model):
    key = models.CharField(max_length=50, unique=True)
    user = models.OneToOneField(
        'Usermodel',
        related_name="auth_tokens",
        on_delete=models.CASCADE,
        verbose_name="user",
        null=True,
        blank=True,
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    session_dict = models.TextField(null=False, default="{}")
    dict_ready = False
    data_dict = None

    def init(self, *args, **kwargs):
        self.dict_ready = False
        self.data_dict = None
        super(Token, self).init(*args, **kwargs)

    def generate_key(self):
        return "".join(
            random.choice(
                string.ascii_lowercase + string.digits + string.ascii_uppercase
            )
            for i in range(40)
        )

    def save(self, *args, **kwargs):
        if not self.key:
            new_key = self.generate_key()
            while type(self).objects.filter(key=new_key).exists():
                new_key = self.generate_key()
            self.key = new_key
        return super(Token, self).save(*args, **kwargs)

    def read_session(self):
        if self.session_dict == "null":
            self.data_dict = {}
        else:
            self.data_dict = json.loads(self.session_dict)
        self.dict_ready = True

    def update_session(self, tdict, save=True, clear=False):
        if not clear and not self.dict_ready:
            self.read_session()
        if clear:
            self.data_dict = tdict
            self.dict_ready = True
        else:
            for key, value in tdict.items():
                self.data_dict[key] = value
        if save:
            self.write_back()

    def set(self, key, value, save=True):
        if not self.dict_ready:
            self.read_session()
        self.data_dict[key] = value
        if save:
            self.write_back()

    def write_back(self):
        self.session_dict = json.dumps(self.data_dict)
        self.save()

    def get(self, key, default=None):
        if not self.dict_ready:
            self.read_session()
        return self.data_dict.get(key, default)

    def __str__(self):
        return str(self.user) if self.user else str(self.id)







            
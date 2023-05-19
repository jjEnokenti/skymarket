from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from .managers import UserManager


class UserRoles:
    USER = 'user'
    ADMIN = 'admin'
    ROLES = ((ADMIN, 'admin'), (USER, 'user'))


class User(AbstractBaseUser):
    first_name = models.CharField(_('first name'), max_length=40)
    last_name = models.CharField(_('last name'), max_length=40)
    email = models.EmailField(_('email address'), unique=True)
    phone = PhoneNumberField(_('phone number'))
    role = models.CharField(max_length=5, choices=UserRoles.ROLES, default=UserRoles.USER)
    image = models.ImageField(upload_to='user_avatars', blank=True, null=True)
    is_active = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    @property
    def full_name(self):
        return f'{self.first_name}, {self.last_name}'

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

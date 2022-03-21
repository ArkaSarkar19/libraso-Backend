from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser,PermissionsMixin, UserManager
)
from django.utils import timezone

from django_code import settings
# Create your models here.
User = settings.AUTH_USER_MODEL

class OurUserManager(UserManager):
    def _create_user(self, username, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        now = timezone.now()
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email,
                          is_staff=is_staff,
                          is_superuser=is_superuser,
                           **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, username, password, email=None, **extra_fields):
        return self._create_user(username, email, password, True, True,
                                 **extra_fields)


class OurUser(AbstractBaseUser,PermissionsMixin):

    class GenderType(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F','Female'
        OTHER = 'O','Other'

    class UserType(models.TextChoices):
        ADMIN = 'AD', 'Admin'
        PROFESSOR = 'PR','PROFESSOR'
        STUDENT = 'ST','STUDENT'

    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )

    objects = OurUserManager()
    first_name = models.CharField(max_length=500, null = True)
    last_name = models.CharField(max_length=500, null = True)

    username = models.CharField(max_length=30, unique=True)
    is_staff = models.BooleanField(('staff status'), default=False) # a admin user; non super-user
    email = models.EmailField(verbose_name='email', max_length=64, unique=True)

    gender = models.CharField(
        max_length=2,
        choices = GenderType.choices,
        default = GenderType.FEMALE
    )
    # notice the absence of a "Password field", that is built in.
    user_type = models.CharField(
        max_length=2,
        choices = UserType.choices,
        default = UserType.STUDENT
    )
    USERNAME_FIELD = 'username'

    def __str__(self):
        return str(self.username)


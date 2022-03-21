from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser,PermissionsMixin
)
from django.utils import timezone

from django_code import settings
# Create your models here.
User = settings.AUTH_USER_MODEL

class UserManager(BaseUserManager):
    def create_user(self, username, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email and password.
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

    def create_professor_user(self, username, email=None, password=None, **extra_fields):
        """
        Creates and saves a staff user with the given email and password.
        """

        return self.create_user(username, email, password, True,False,**extra_fields)

    def create_admin_user(self, username, email=None, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """

        return self.create_user(username, email, password, True,True,**extra_fields)



class User(AbstractBaseUser,PermissionsMixin):

    class GenderType(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F','Short'
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

    objects = UserManager()
    first_name = models.CharField(max_length=500, null = True)
    last_name = models.CharField(max_length=500, null = True)


    username = models.CharField(max_length=30, unique=True)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser
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
    REQUIRED_FIELDS = [] # Email & Password are required by default.

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin


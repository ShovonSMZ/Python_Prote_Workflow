from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class MyAccountManager(BaseUserManager):
	def create_user(self, first_name, last_name, email, username, password=None):
		if not first_name:
			raise ValueError('Please enter your first name')
		if not last_name:
			raise ValueError('Please enter your last name')
		if not email:
			raise ValueError('Users must have a valid email address')
		if not username:
			raise ValueError('Please set a username')

		user = self.model(
			first_name		= first_name,
			last_name		= last_name,
			email			= self.normalize_email(email),
			username		= username,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, first_name, last_name, email, username, password):
		user = self.create_user(
			first_name		= first_name,
			last_name		= last_name,
			email			= self.normalize_email(email),
			username		= username,
			password		= password,
		)
		user.is_admin		= True
		user.is_staff		= True
		user.is_superuser	= True
		user.save(using=self._db)
		return user


class Account(AbstractBaseUser):
	first_name		= models.CharField(verbose_name='First Name', max_length=30)
	last_name		= models.CharField(verbose_name='Last Name', max_length=30)
	email 			= models.EmailField(verbose_name="Email", max_length=60, unique=True)
	username 		= models.CharField(max_length=30, unique=True)
	date_joined		= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login		= models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin		= models.BooleanField(default=False)
	is_active		= models.BooleanField(default=True)
	is_staff		= models.BooleanField(default=False)
	is_superuser	= models.BooleanField(default=False)


	USERNAME_FIELD	= 'username'
	REQUIRED_FIELDS	= ['first_name','last_name','email']

	objects = MyAccountManager()

	def __str__(self):
		return self.first_name +" "+self.last_name

	# For checking permissions. Admin have ALL permissons
	def has_perm(self, perm, obj=None):
		return self.is_admin

	# Does this user have permission to view this app?
	def has_module_perms(self, app_label):
		return True

	def get_short_name(self):
		return self.first_name

	def get_full_name(self):
		return self.first_name +" "+self.last_name

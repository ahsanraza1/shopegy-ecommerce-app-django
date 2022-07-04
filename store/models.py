# from distutils.command.upload import upload
# from email.policy import default
# from django.forms import ImageField


from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

class WoztiUserManager( BaseUserManager) :
    def create_user( self, email, name, password= None):
        if not email :
            raise ValueError(" Email is required")
        if not name :
            raise ValueError("Name is required")
        
        user = self.model(
            email = self.normalize_email(email),
            name = name
        )

        user.set_password(password)
        user.save( using=self._db)
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(
            email=self.normalize_email(email),
            name=name,
            password=password
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save( using=self._db)
        return user

class WoztiUser( AbstractBaseUser ):
    email = models.EmailField( verbose_name="Email Address", max_length=60, unique=True)
    name  = models.CharField( verbose_name="User Name", max_length=200)
    date_joined = models.DateTimeField( verbose_name="Joined At", auto_now_add=True)
    last_login  = models.DateTimeField( verbose_name="Last login", auto_now=True )
    password     = models.CharField(max_length=100)
    is_admin     = models.BooleanField(default=False)
    is_active    = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff     = models.BooleanField(default=False)
    hide_email = models.BooleanField(default=True)    
    # profile_image = ImageField( max_length=255, upload_to='', null=True, blank=True, default='')
    
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS= ['name']

    objects = WoztiUserManager()    

    def __str__(self):
        return self.email
    
    def has_perm( self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms( self, app_label):
        return True

# #####################   Models Here 
#  Category Class

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(
        max_length=250,
        default='',
        blank=True,
        null=True)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()
  
    def __str__(self):
        return self.name

#  Product class 

class Product(models.Model):
    name = models.CharField(max_length=60)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
    description = models.CharField(
        max_length=250, default='', blank=True, null=True)

    Rating = (
        (0, "0"),
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5")
    )
    rating = models.PositiveIntegerField(default = 0, choices= Rating, null = True, blank = True)
    image = models.ImageField( null=True, blank=True, upload_to='images/')
    image1 = models.ImageField( null=True, blank=True, upload_to='images/')
    image2 = models.ImageField( null=True, blank=True, upload_to='images/')
    image3 = models.ImageField( null=True, blank=True, upload_to='images/')
    image4 = models.ImageField( null=True, blank=True, upload_to='images/')
    
    # image = models.CharField(
    #     max_length=1000, default='', blank=True, null=True)
  
    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)
  
    @staticmethod
    def get_all_products():
        return Product.objects.all()
  
    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()
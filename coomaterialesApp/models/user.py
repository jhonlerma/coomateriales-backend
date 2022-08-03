from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager ):
    def create_user(self, username, password = None):
        # Creación del usuario
        if not username:
            # Validación si el usuario ya existe
            raise ValueError('Usuario ya existente')
        user = self.model(username = username)
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser (self, username, password = None):
        # Creación del super usuario
        user = self.create_user(username= username, password=password,)
        user.is_admin = True
        user.save(using = self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    # Creación de la tabla de la base de datos
    id = models.BigAutoField(primary_key=True)
    username = models.CharField('Username', max_length=30, unique=True)
    password = models.CharField('Password', max_length=256)
    nombre_usuario = models.CharField('Name', max_length= 40)
    apellido_usuario = models.CharField('LastName',max_length=40)
    telefono_usuario = models.CharField('Phone', max_length=40)
    correo_usuario = models.EmailField('Email', max_length=256)
    direccion_usuario = models.CharField('Address', max_length=60)

    def save(self, **Kwargs):
        # Creación de encriptación de la contraseña
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**Kwargs)
    objects = UserManager()
    USERNAME_FIELD = 'username'
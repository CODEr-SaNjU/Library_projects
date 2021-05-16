from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, Mob_Number, Email, password, **extra_fields):
        """
        create and save  a User with the given email and password
        """
        if not Email:
            raise ValueError(
                'The User must have an  Email address')
        Email = self.normalize_email(Email)
        user = self.model(
            Email=Email,
            Mob_Number=Mob_Number,
            **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, Email, Mob_Number, password, **extra_fields):
        """
        create and save a staff user with the given email and password
        """
        extra_fields.setdefault('is_superuser', False)
        user = self._create_user(
            Email=Email,
            Mob_Number=Mob_Number,
            password=password,

        )
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, Email, Mob_Number, password, **extra_fields):
        """
        creates and saves a superuser with the given email and password
        """
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('SuperUser must have is_superuser =True')
        user = self._create_user(
            Email=Email,
            Mob_Number=Mob_Number,
            password=password,

        )
        user.is_staff = True
        user.admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

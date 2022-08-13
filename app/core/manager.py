from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_field):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            **extra_field
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_field):
        """
        Creates and saves a superuser with the given email & password.
        """
        user = self.create_user(
            email,
            password=password,
            **extra_field
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

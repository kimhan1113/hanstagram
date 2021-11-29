from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

import uuid

# Create your models here.

class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = "M", "남성"
        FEMALE = "F", "여성"


    website_url = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    phone_number = models.CharField(max_length=13, blank=True, validators=[RegexValidator(r"^$010-?[0-9]\d{4}-?\d{4}$")])
    gender = models.CharField(max_length=1, blank=True, choices=GenderChoices.choices)
    avatar = models.ImageField(blank=True, upload_to="accounts/avatar/%Y/%m/%d", help_text="24x24 이미지 사이즈")

    # email_verified = models.BooleanField(default=False)
    # email_secret = models.CharField(max_length=20, default="", blank=True)

    # def save(self, *args, **kwargs):
    #     # is_created = (self.pk == None)
    #     # super().save(*args, **kwargs)


    # def verify_email(self):
    #     if self.email_verified is False:
    #         secret = uuid.uuid4().hex[:20]
    #         self.email_secret = secret
    #         html_message = render_to_string(
    #             "accounts/verify_email.html", {"secret": secret}
    #         )
    #         send_mail(
    #             "Verify Hanstagram Account",
    #             strip_tags(html_message),
    #             settings.EMAIL_FROM,
    #             [self.email],
    #             html_message=html_message,
    #         )
    #
    #         self.save()
    #     return

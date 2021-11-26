from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

import uuid

# Create your models here.

class User(AbstractUser):
    website_url = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    email_verified = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=20, default="", blank=True)

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

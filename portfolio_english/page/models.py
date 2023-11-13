from django.db import models


# Create your models here.
class landingpage(models.Model):
    profile_pic = models.FileField(
        upload_to="profile/", max_length=300, null=True, default=None
    )
    name = models.CharField(max_length=100)  # cannot be null or blank
    role = models.CharField(max_length=100)
    mail = models.EmailField(default="hello@reallygreatsite.com")
    linkedin = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)


class aboutussection(models.Model):
    aboutme_description = models.CharField(max_length=1000)
    cover_pic_for_aboutme = models.FileField(
        upload_to="aboutme/", max_length=100, null=True, default=None
    )


class experienceandeducation(models.Model):
    start_year = models.CharField(max_length=4)
    work_role = models.CharField(max_length=50)
    work_place = models.CharField(max_length=100)
    work_description = models.CharField(max_length=500)


class skills(models.Model):
    classroom_point1 = models.CharField(max_length=100)
    classroom_point2 = models.CharField(max_length=100)
    module_design_point1 = models.CharField(max_length=100)
    module_design_point2 = models.CharField(max_length=100)


class volunteersection(models.Model):
    # Image
    volunteer_cover_pic = models.FileField(
        upload_to="volunteer/", max_length=100, null=True, default=None
    )
    volunteer_place = models.CharField(max_length=100)
    volunteer_description = models.CharField(max_length=1000)

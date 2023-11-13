from django.shortcuts import render

# from django.http import HttpResponse

# models page
from .models import (
    landingpage,
    aboutussection,
    experienceandeducation,
    skills,
    volunteersection,
)


# Create your views here.
def home(request):
    # landing page
    landingdata = landingpage.objects.all().first()

    # about me
    aboutmedata = aboutussection.objects.all().first()

    # experience and education
    experiencedata = experienceandeducation.objects.all().order_by("-id")[:3]

    for exp_data in experiencedata:
        print()

    # skills
    skillsdata = skills.objects.all().first()

    # volunteer
    volunteerdata = volunteersection.objects.all()[:3]
    
    for vol_data in volunteerdata:
        print()

    # footer
    sitedata = {
        "landingdata": landingdata,
        "aboutmedata": aboutmedata,
        "experiencedata": experiencedata,
        "skillsdata": skillsdata,
        "volunteerdata": volunteerdata,
    }

    return render(request, "index.html", sitedata)

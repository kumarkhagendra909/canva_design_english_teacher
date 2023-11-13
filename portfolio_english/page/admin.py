from django.contrib import admin
from page.models import landingpage, aboutussection, experienceandeducation, skills, volunteersection

# Register your models here.
class LandingpageAdmin(admin.ModelAdmin):
    list_display = ('name', 'role')

admin.site.register(landingpage, LandingpageAdmin)

class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('aboutme_description',)

admin.site.register(aboutussection , AboutMeAdmin)


class ExperienceandEducationAdmin(admin.ModelAdmin):
    list_display = ('start_year', 'work_role', 'work_place', 'work_description')

admin.site.register(experienceandeducation ,ExperienceandEducationAdmin)

class skillsAdmin(admin.ModelAdmin):
    list_display = ('classroom_point1', 'classroom_point2', 'module_design_point1', 'module_design_point2')

admin.site.register(skills ,skillsAdmin)

class volunteerAdmin(admin.ModelAdmin):
    list_display = ('volunteer_place', 'volunteer_description')

admin.site.register(volunteersection ,volunteerAdmin)
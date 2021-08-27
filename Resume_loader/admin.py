from django.contrib import admin

# Register your models here.
from .models import  Resume

@admin.register(Resume)
class ResumeModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','dob','gender','locality','city','pin','state','mobile','Current_city','Prefered_Job_City','Profile_image','myfile']


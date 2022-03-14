from django.contrib import admin
from metaconnect.models import ProjectDetails,Owner,ArchiveProjectDetails

# Register your models here.
admin.site.register(ProjectDetails)
admin.site.register(Owner)
admin.site.register(ArchiveProjectDetails)

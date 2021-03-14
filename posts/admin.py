from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import PostModel, AssuntoModel, ComentarioModel

# Register your models here.
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('corpo', )

admin.site.register(PostModel, PostAdmin)
admin.site.register(AssuntoModel)
admin.site.register(ComentarioModel)

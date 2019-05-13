from django.contrib import admin
from .models import Post # the . just means current dir
# Register your models here. to make them show up on admin page

admin.site.register(Post)

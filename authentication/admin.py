from django.contrib import admin
from .models import User

# Register your models here.
# from .models import User
#
#
class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)
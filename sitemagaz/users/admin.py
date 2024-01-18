from django.contrib import admin
from carts.admin import CartTabAdmin
from users.models import User
# Register your models here.

# admin.site.register(User)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username","last_name", "first_name", 'email']
    search_fields = ["username","last_name", "first_name", 'email']
    inlines= [CartTabAdmin]
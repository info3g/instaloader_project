from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(groupa_users)

admin.site.register(groupb_users)


admin.site.register(groupA_all_users)

admin.site.register(groupB_all_users)
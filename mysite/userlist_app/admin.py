from django.contrib import admin
from userlist_app.models import User
from userlist_app.models import ChatMessage


admin.site.register(User)
admin.site.register(ChatMessage)
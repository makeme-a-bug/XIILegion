from django.contrib import admin
from .models import profile,Posts,Thread,Thread_category,thread_reply,post_reply,games
from django.contrib.auth.models import Permission

admin.site.register(profile)
admin.site.register(Posts)
admin.site.register(Thread)
admin.site.register(Thread_category)
admin.site.register(thread_reply)
admin.site.register(post_reply)
admin.site.register(games)

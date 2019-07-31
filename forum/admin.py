from django.contrib import admin
from .models import Question
from .models import Answer
from .models import Comments

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Comments)

# Register your models here.

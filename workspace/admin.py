from django.contrib import admin
from .models import WorkSpace, Member, TaskComment, Timeline, Task, Scrum

# Register your models here.
admin.site.register(WorkSpace)
admin.site.register(Member)
admin.site.register(TaskComment)
admin.site.register(Timeline)
admin.site.register(Task)
admin.site.register(Scrum)

from django.contrib import admin
from score.models import Score
# Register your models here.
class ScoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'value']
    
    
admin.site.register(Score, ScoreAdmin)
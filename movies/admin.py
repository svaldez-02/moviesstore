from django.contrib import admin
from .models import Movie, Review


class MovieAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']


class ReviewAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'movie',
        'user',
        'date',
        'reported'
    ]

    list_filter = [
        'reported',
        'date'
    ]

    search_fields = [
        'comment',
        'user__username',
        'movie__name'
    ]

    ordering = ['-date']


admin.site.register(Movie, MovieAdmin)
admin.site.register(Review, ReviewAdmin)
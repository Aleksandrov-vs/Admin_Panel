from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Genre, Filmwork, GenreFilmwork, Person, PersonFilmwork


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


class PersonFilmworkInline(admin.TabularInline):
    model = PersonFilmwork
    verbose_name = _('Person who worked on the film')


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    inlines = (PersonFilmworkInline,)

    def category_post_count(self, obj):
        return obj.filmwork_set.count()

    category_post_count.short_description = _('count works')

    list_display = ('full_name', 'category_post_count')


class GenreFilmworkInline(admin.TabularInline):
    model = GenreFilmwork
    verbose_name = _('Genres of the film')


@admin.register(Filmwork)
class FilmworkAdmin(admin.ModelAdmin):
    inlines = (GenreFilmworkInline, PersonFilmworkInline)

    list_display = ('title', 'type', 'creation_date', 'rating',)

    list_filter = ('type', 'creation_date')

    search_fields = ('title', 'description', 'id')

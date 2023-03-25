import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator


class TimeStampedMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Genre(UUIDMixin, TimeStampedMixin):
    name = models.CharField('name', max_length=255)
    description = models.TextField('description', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "content\".\"genre"
        verbose_name = _('Genre')
        verbose_name_plural = _('Genres')


class TypyFilmwork(models.TextChoices):
    MOVIE = 'movie', _('Moive')
    TV_SHOW = 'tv_show', _('Tv Show')


class Person(UUIDMixin, TimeStampedMixin):
    full_name = models.TextField(_('full_name'), null=False)

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = "content\".\"person"
        verbose_name = _('Person')
        verbose_name_plural = _('Persons')


class Filmwork(UUIDMixin, TimeStampedMixin):

    title = models.TextField(_('title'))
    description = models.TextField(_('description'), blank=True, null=True)
    creation_date = models.DateField(_('creation_date'), blank=True, null=True)
    rating = models.FloatField(_('rating'), blank=True, null=True,
                               validators=[MinValueValidator(0),
                                           MaxValueValidator(100)])
    type = models.TextField(_('type'), choices=TypyFilmwork.choices)
    genres = models.ManyToManyField(Genre, through='GenreFilmwork')
    persons = models.ManyToManyField(Person, through='PersonFilmwork')

    def __str__(self):
        return self.title

    class Meta:
        db_table = "content\".\"film_work"
        verbose_name = _('Filmwork')
        verbose_name_plural = _('Filmworks')


class GenreFilmwork(UUIDMixin):
    film_work = models.ForeignKey('Filmwork', on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "content\".\"genre_film_work"
        unique_together = (('film_work', 'genre'),)


class PersonFilmwork(UUIDMixin):
    person = models.ForeignKey('Person', models.DO_NOTHING)
    film_work = models.ForeignKey('Filmwork', models.DO_NOTHING)
    role = models.TextField()
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "content\".\"person_film_work"
        unique_together = (('film_work', 'person', 'role'),)

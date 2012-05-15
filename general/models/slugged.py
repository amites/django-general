from django.db import models

from general.unique_slugify import unique_slugify


class Slugged(models.Model):
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if self.slug == '':
            try:
                name = self.slug_name
            except AttributeError:
                try:
                    name = self.name
                except AttributeError:
                    raise Exception('Model %s must have field `name`' \
                        + 'or define `slug_name`' % self._meta.object_name)
            self.slug = unique_slugify(self, name)

        super(Slugged, self).save(*args, **kwargs)

    class Meta:
        abstract = True
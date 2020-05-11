from django.db import models


class Location(models.Model):
    """When creating a gamenight, or a play, add location to the game

    Location can either be private or public, players have access to create gamenight with locations that are public, or the private locations of friends.

    A business can later verify ownership
    """
    name = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    zip = models.IntegerField(null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    public = models.BooleanField(
        default=False,
        help_text=
        'Is this location a public location? ex. Cafe, Pub, Library, etc')

    def __str__(self):
        return self.name
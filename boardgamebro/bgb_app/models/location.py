from django.db import models


class Location(models.Model):
    """When creating a gamenight, or a play, add location to the game

    Location can either be private or public, players have access to create gamenight with locations that are public, or the private locations of friends.

    A business can later verify ownership
    """
    name = models.CharField(max_length=30)
    description = models.TextField()
    address = models.CharField(max_length=50)
    zip = models.IntegerField()
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    # type (home, cafe, pub)
    public = models.BooleanField(
        default=False,
        help_text=
        'Is this location a public location? ex. Cafe, Pub, Library, etc')

from django.db import models
from django.utils.text import slugify
from django import template
from django.contrib.auth import get_user_model  # get the user model currently active in this project
import misaka

# slugify:
# if there is a string you want to use that as part of your url,
# it's going to be able to lowercase and add dashes instead of spaces

User = get_user_model()  # get user models in this project
register = template.Library()  # this is how we can use custom template tags in the future


class Group(models.Model):
    name = models.CharField(max_length=256, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False, default='', blank=True)
    members = models.ManyToManyField(User, through='GroupMember')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)



class GroupMember(models.Model):
    group = models.ForeignKey(Group, related_name='memberships', on_delete=models.CASCADE)
    # this means the groupMember is linked to group by the 'memberships' foreignKey
    user = models.ForeignKey(User, related_name='user_groups', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('group', 'user')

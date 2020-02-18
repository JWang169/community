from django.db import models
from django.utils.text import slugify

# slugify:
# if there is a string you want to use that as part of your url,
# it's going to be able to lowercase and add dashes instead of spaces
import misaka

from django.contrib.auth import get_user_model  # get the user model currently active in this project
User = get_user_model()  # get user models in this project


from django import template
register = template.Library()  # this is how we can use custom template tags in the future


class Group(models.Model):
    pass

class GroupMember(models.Model):
    group = models.ForeignKey(Group, related_name='memberships', on_delete=models.CASCADE)
    # this means the groupMember is linked to group by the 'memberships' foreignKey
    user = models.ForeignKey(User, related_name='user_groups', on_delete=models.CASCADE)

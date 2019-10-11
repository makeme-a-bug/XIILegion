from django import template

register = template.Library()

@register.filter(name='has_group')
def has_group(user, name):
    if name =='can edit post':
        if user.groups.filter(name="The emperor").exists():
            return True
    #     elif user.groups.filter(name="The emperor").exists():
    #         return True
    if name =='can delete post':
        if user.groups.filter(name="The emperor").exists():
            return True
    #     elif user.groups.filter(name="The emperor").exists():
    #         return True
    if name =='can create post':
        if user.groups.filter(name="The emperor").exists():
            return True
    #     elif user.groups.filter(name="The emperor").exists():
    #         return True
    if name =='can create thread_category':
        if user.groups.filter(name="The emperor").exists():
            return True
    #     elif user.groups.filter(name="The emperor").exists():
    #         return True
    if name =='can delete thread_category':
        if user.groups.filter(name="The emperor").exists():
            return True
    #     elif user.groups.filter(name="The emperor").exists():
    #         return True
    if name =='can edit thread_category':
        if user.groups.filter(name="The emperor").exists():
            return True
    #     elif user.groups.filter(name="The emperor").exists():
    #         return True
    if name =='can create thread':
        if user.groups.filter(name="The emperor").exists():
            return True
        elif user.groups.filter(name="The commoner").exists():
            return True
    if name =='can delete thread':
        if user.groups.filter(name="The emperor").exists():
            return True
        elif user.groups.filter(name="The commoner").exists():
            return True
    if name =='can edit thread':
        if user.groups.filter(name="The emperor").exists():
            return True
        elif user.groups.filter(name="The commoner").exists():
            return True

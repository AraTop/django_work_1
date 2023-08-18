from django.http import Http404
from django.contrib.auth.models import Group

class AuthorPermissionsMixin:
    def has_permissions(self):
        return self.get_object().user == self.request.user
    
    def dispatch(self, request, *args, **kwargs):
        if not self.has_permissions():
            raise Http404()
        return super().dispatch(request, *args, **kwargs)
    
class ModeratorPermissionsMixin(AuthorPermissionsMixin):
    def has_permissions(self):
        is_author = super().has_permissions()

        if is_author:
            return True

        return self.request.user.groups.filter(name='moderator').exists()
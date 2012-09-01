from django.db import models
from mezzanine.pages.models import Page

class Splash(Page):
	splash_page	= models.CharField(null=True, max_length=50)
        def can_add(self, request):
                return self.children.count() == 0

        def can_delete(self, request):
                return request.user.is_superuser or self.parent is not None



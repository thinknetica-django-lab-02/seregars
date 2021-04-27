from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.db import models

from ckeditor.widgets import CKEditorWidget

from main.models import Product, Category, Tag, Profile


class FlatPageEdit(FlatPageAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageEdit)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Profile)
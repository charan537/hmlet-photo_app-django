import django_tables2 as tables
from PhotoApp.models import Photo
from django.utils.safestring import mark_safe
from django.utils.html import escape
from django_tables2.utils import A
from crequest.middleware import CrequestMiddleware

class ImageColumn(tables.Column):
    def render(self, value):
        return mark_safe('<img src="%s" class="img" />'% escape(value.url))

class PhotoTable(tables.Table):
    image  = ImageColumn('image')
    edit = tables.LinkColumn('photo_update', args=[A('pk')], orderable=False, empty_values=())
    delete = tables.LinkColumn('photo_delete', args=[A('pk')], orderable=False, empty_values=())
    class Meta:
        model = Photo
        template_name = "django_tables2/bootstrap.html"
        fields = ('title','image','captions','saveAsDraft','publishedDate','user')

    def render_edit(self, record):
        current_request = CrequestMiddleware.get_request()
        if record.user != current_request.user:
            return ''
        return 'Edit'
    def render_delete(self,record):
        current_request = CrequestMiddleware.get_request()
        if record.user != current_request.user:
            return ''
        return 'Delete'

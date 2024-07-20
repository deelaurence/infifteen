from django.contrib import admin
from .models import Question,Category

class PublishFilter(admin.SimpleListFilter):
    title = 'Publish Status'
    parameter_name = 'publish'

    def lookups(self, request, model_admin):
        return (
            ('all', 'All'),
            ('unpublished', 'Unpublished'),
            ('published', 'Published'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'published':
            return queryset.filter(publish=True)
        elif self.value() == 'unpublished':
            return queryset.filter(publish=False)
        elif self.value() == 'all':
            return queryset.all()

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'category', 'publish')
    list_filter = (PublishFilter,)
    search_fields = ('question_text', 'category')


admin.site.register(Category)

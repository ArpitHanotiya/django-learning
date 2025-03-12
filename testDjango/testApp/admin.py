from django.contrib import admin
from .models import testAppVariety, testAppReview, store, testAppCertificate

# Register your models here.
class testAppReviewInLine(admin.TabularInline):
    model = testAppReview
    extra = 2

class testAppVarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')
    inlines = [testAppReviewInLine]

class storeAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('app_varities', )

class testAppCertificateAdmin(admin.ModelAdmin):
    list_display = ('app', 'certificate_number')

admin.site.register(testAppVariety, testAppVarietyAdmin)
admin.site.register(store, storeAdmin)
admin.site.register(testAppCertificate, testAppCertificateAdmin)

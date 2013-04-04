from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'extrapole.views.home', name='home'),
    url(r'^maildir/', include('django_maildir.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

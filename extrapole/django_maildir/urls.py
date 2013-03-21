from django.conf.urls import patterns, include, url

urlpatterns = patterns('django_maildir.views',
    url(r'^$', 'index', name='maildir_index'),
)

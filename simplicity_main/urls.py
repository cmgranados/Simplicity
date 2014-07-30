from django.conf.urls import patterns, include, url

from django.contrib import admin
from kappa.requirements.views import RequirementListView
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'simplicity_main.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^kappa/requirements/$', RequirementListView.as_view(), name='requirement-list'),
)

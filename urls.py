from django.conf.urls.defaults import *
from ujourney.views import *
#from ujourney.registration import *
from ujourney.level1 import *
from ujourney.models import *
from django.views.generic import list_detail
from django.conf import settings
from ujourney.level0 import *


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
	
article_info = {
    "queryset" : Article.objects.all(),
	"template_name": "level1/article_list.html",
}

user_info = {
    "queryset" : Users.objects.all(),
	"template_name": "level1/profile.html",
}

urlpatterns = patterns('',
	(r'^level0/register/$', registration),
	(r'^level0/yeah/$', registration_save),
    (r'^level0/rules/$', rules_of_the_game),
    (r'^level0/user_agreement/$', user_agreement),
	(r'^$', main),
	(r'^level1/add/$', add_article),
	(r'^level1/profile/$', list_detail.object_list, user_info),
	(r'^level1/$', list_detail.object_list, article_info),
	(r'^level1/articles/$',  list_detail.object_list, article_info),
    (r'^level1/login/$',  login),

	#(r'^login/$', login),
    # Example:
    # (r'^megaproject/', include('megaproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )



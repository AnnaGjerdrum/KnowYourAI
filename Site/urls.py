from django.urls import path
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    url(r'^$', views.index_view.as_view(), name='index'),

# what is AI?
    url(r'^input/$', views.input, name='input'),
    url(r'^data/$', views.data, name='data'),
    url(r'^learning/$', views.learning, name='learning'),
    url(r'^mistakes/$', views.mistakes, name='mistakes'),
    url(r'^output/$', views.output, name='output'),

# usage
    url(r'^where/$', views.where, name='where'),
    url(r'^why/$', views.why, name='why'),
    url(r'^jobs/$', views.jobs, name='jobs'),
    url(r'^jobs2/$', views.jobs2, name='jobs2'),
    url(r'^danger/$', views.danger, name='danger'),

# ethics
    url(r'^ethics/$', views.ethics, name='ethics'),
    url(r'^privacy/$', views.privacy, name='privacy'),
    url(r'^influence/$', views.influence, name='influence'),
    url(r'^weapons/$', views.weapons, name='weapons'),
    url(r'^account/$', views.account, name='account'),

# teach your AI
    url(r'^game/$', views.game, name='game'),
    url(r'^object/$', views.object, name='object'),
    url(r'^language/$', views.language, name='language'),

# algorithms
    url(r'^OAlgo/$', views.OAlgo, name='OAlgo'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#add new page (url)
 #url(r'^URL/$', views.URL, name='URL'),
 # also add in views

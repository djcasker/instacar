from django.conf.urls import url

import home.views 

urlpatterns = [
    url(r'^$', home.views.homepage, name='homepage'),
]
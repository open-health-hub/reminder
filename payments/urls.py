from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from .views import SubscribeView, SuccessView

urlpatterns = patterns(
    '',
    url(r'^subscribe/$', login_required(SubscribeView.as_view()), name='subscribe'),
    url(r'^thank_you/$', login_required(SuccessView.as_view()), name='thank_you'),
)

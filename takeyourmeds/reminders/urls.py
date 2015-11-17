from django.conf.urls import url, include

from . import views

urlpatterns = (
    url(r'', include('takeyourmeds.reminders.reminders_calls.urls',
        namespace='calls')),
    url(r'', include('takeyourmeds.reminders.reminders_messages.urls',
        namespace='messages')),

    url(r'^reminders/new$', views.create,
        name='create'),
    url(r'^reminders/reminder/(?P<reminder_id>\d+)/delete$', views.delete,
        name='delete'),
    url(r'^reminders/reminder/(?P<reminder_id>\d+)/trigger$', views.trigger,
        name='trigger'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'djcelery',
    'email_from_template',
    'rest_framework',

    'takeyourmeds.account',
    'takeyourmeds.api',
    'takeyourmeds.groups',
    'takeyourmeds.groups.groups_admin',
    'takeyourmeds.groups.groups_billing',
    'takeyourmeds.profile',
    'takeyourmeds.registration',
    'takeyourmeds.reminders',
    'takeyourmeds.static',
    'takeyourmeds.telephony',
    'takeyourmeds.utils',
)

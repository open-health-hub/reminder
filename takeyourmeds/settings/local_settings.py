# A secret key!
SECRET_KEY = 'wombles'

# Your Twilio account SID
TW_ACCOUNT_SID="xxxxxx"

# Your twilio account SID
TW_AUTH_TOKEN="xxxxxxx"

# Your twilio SMS-enabled phone number
TW_FROM_NUMBER="+44......"

# The root URL from where the Twilio service can pick
# up the TwilML because Ross is too lazy to work out the
# server name dynamically.
TW_ROOT_URL="http://127.0.0.1:8000/telephony/info"

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

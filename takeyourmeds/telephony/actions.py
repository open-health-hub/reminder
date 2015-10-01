import os
import uuid
import urlparse

from django.conf import settings
from django.core.urlresolvers import reverse

from twilio.rest import TwilioRestClient

def send_sms(to_number, message_text):
    """
    Send SMS message.
    """

    if not settings.TWILIO_ENABLED:
        return 'dummy-sid'

    config = settings.TWILIO_CONFIG

    message = _get_client().messages.create(
        to=to_number,
        body=message_text,
        from_=config['FROM_NUMBER'],
    )

    return message.sid

def make_call(to_number, audio_url):
    """
    Make a call to the specified number and play the MP3 specified in
    `audio_url`.
    """

    if not settings.TWILIO_ENABLED:
        return 'dummy-sid'

    name = str(uuid.uuid4())

    config = settings.TWILIO_CONFIG

    # Write out the XML with the URL of the audio
    _write_twiml(name, audio_url)

    callback_url = urlparse.urljoin(
        settings.SITE_URL,
        reverse('info', kwargs={'uuid': name})
    )

    call = _get_client().calls.create(
        to=to_number,
        from_=config['FROM_NUMBER'],
        url=callback_url,
        method='GET',
        fallback_method='GET',
        status_callback_method='GET',
        record='false',
    )

    return call.sid

def _write_twiml(name, audio_url):
    # Generate XML file, save with name
    with open(os.path.join("/tmp", name + ".xml"), "w") as f:
        doc = """
            <?xml version="1.0" encoding="UTF-8"?>
            <Response>
                <Play loop="1">{}</Play>
            </Response>
        """.format(audio_url)
        f.write(doc.strip())

def _get_config():
    return settings.TWILIO_CONFIG

def _get_client():
    config = settings.TWILIO_CONFIG

    return TwilioRestClient(config["ACCOUNT_SID"], config["AUTH_TOKEN"])

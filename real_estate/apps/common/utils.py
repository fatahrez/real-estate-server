from django.core.mail import send_mail
from django.template.loader import render_to_string

from real_estate.config.settings.base import EMAIL_HOST_USER, env


def send_link(**kwargs):
    token = kwargs.get('token')
    email = kwargs.get('email')
    subject = kwargs.get('subject')
    url = kwargs.get('url')
    template = kwargs.get('template')

    from_email, to_email = EMAIL_HOST_USER, email
    base_url = env('BASE_URL')

    link = '{0}{1}{2}'.format(str(base_url), str(url), str(token))

    message = render_to_string(
        template, {
            'user': to_email,
            'token': token,
            'username': to_email,
            'link': link
        })
    send_mail(subject, '', from_email,
              [to_email, ], html_message=message, fail_silently=False)
from threading import Thread

from django.core.mail import EmailMessage
from django.template.loader import render_to_string


def send_template_mail(to: [str], subject: str, template: str, context: dict,
                       from_email: str = None, fail_silently: bool = True,
                       asynchronously: bool = True):
    html = render_to_string(template, context)
    e_message = EmailMessage(
        subject=subject,
        body=html,
        from_email=from_email,
        to=to,
    )
    e_message.content_subtype = 'html'
    if not asynchronously:
        e_message.send(fail_silently=fail_silently)
    else:
        # TODO: we have to use Celery here
        Thread(
            target=e_message.send,
            kwargs={'fail_silently': fail_silently}
        ).start()

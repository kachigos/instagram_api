from django.core.mail import send_mail


def send_reset_password(self):
    import uuid
    code = str(uuid.uuid4())
    self.activation_code = code

    to_email = 'chyngyzsubhanov@gmail.com'
    send_mail(
        'Subject',
        f'Your code for reset {code} password: ',
        'from@example.com',
        [to_email,],
        fail_silently=False
    )


def send_notification(profile):
    to_email = 'chyngyzsubhanov@gmail.com'
    send_mail(
        f'{profile} added new post',
        f'чекни его(ее) пост !!',
        'from@example.com',
        [to_email,],
        fail_silently=False
    )
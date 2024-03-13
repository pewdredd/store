from celery import shared_task

from users.models import EmailVerification
import uuid
from datetime import timedelta
from django.utils.timezone import now
from users.models import User


@shared_task
def send_verification_email(user_id):
    user = User.objects.get(id=user_id)
    expiration = now() + timedelta(hours=48)
    record = EmailVerification.objects.create(user=user, code=uuid.uuid4(), expiration=expiration)
    record.send_verification_email()


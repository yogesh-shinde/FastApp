from time import sleep
from celery import shared_task

from .models import Service
from .serializations import ServiceSerializer


@shared_task
def update_service():
    print('Updating data ..')

    rows = Service.objects.all()

    for row in rows:
        print({'service id': row.service_id, 'service name': row.service_name,
               'service type': row.service_type, 'service product': row.service_product,
               'service description': row.service_description, 'service verify': row.service_verify,
               'service email': row.service_email, 'user': row.user})
        data = {'service_id': row.service_id, 'service_name': row.service_name,
                'service_type': row.service_type, 'service_product': row.service_product,
                'service_description': row.service_description, 'service_verify': row.service_verify,
                'service_email': row.service_email, 'user': row.user}

        Service.objects.filter(service_id=row.service_id).update(**data)
        sleep(3)


while True:
    sleep(15)
    update_service()

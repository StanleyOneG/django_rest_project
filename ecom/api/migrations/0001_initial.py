from django.db import migrations
from api.user.models import CustomUser


class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user = CustomUser(name="stas", email="goncharuk.sm@yandex.ru", is_staff=True, is_superuser=True, phone="79584551509", gender="Male")

        user.set_password("12345")
        user.save()

    dependencies = [

    ]

    operations = [
        migrations.RunPython(seed_data),
    ]

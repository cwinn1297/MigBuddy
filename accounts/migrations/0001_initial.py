# Generated manually to remove the custom User model

from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        # This migration removes the custom User model that was previously created
        # Since we want to use Django's default User model instead
    ]

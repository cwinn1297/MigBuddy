# Remove the custom User model and go back to Django's default User model

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        # Delete the custom User model table
        migrations.RunSQL(
            "DROP TABLE IF EXISTS accounts_user CASCADE;",
            reverse_sql=migrations.RunSQL.noop
        ),
    ]

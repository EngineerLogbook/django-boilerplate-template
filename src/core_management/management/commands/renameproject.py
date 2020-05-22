from django.core.management.base import BaseCommand, CommandError
import os

class Command(BaseCommand):
    help = "Renames the django project to something of your choosing"

    def add_arguments(self, parser, *args, **kwargs):
        parser.add_argument('newProjName', type=str, help="The name of the new django project.")

    def handle(self, *args, **kwargs):
        newProjName = kwargs['newProjName']

        # Rename project (Specific to django 3.0)
        # Remove asgi.py if using django < 3.0

        list_o_files_to_change = [
            'boilerplate/settings/base_settings.py',
            'boilerplate/wsgi.py',
            'boilerplate/asgi.py',
            'manage.py',
        ]

        folder_to_rename = "boilerplate"

        for thefile in list_o_files_to_change:
            with open(thefile, 'r') as file:
                filedata = file.read()
            
            filedata = filedata.replace('boilerplate', newProjName)


            with open(thefile, 'w') as file:
                file.write(filedata)
        
        try:

            os.rename(folder_to_rename, newProjName)
            self.stdout.write(self.style.SUCCESS(f"Project has been renamed to {newProjName}"))
        
        except:
            raise CommandError('Folder "%s" does not exist' % folder_to_rename)

        
        
        
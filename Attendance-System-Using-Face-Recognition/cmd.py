



import subprocess
from django.core.management.base import BaseCommand
class Command(BaseCommand):
    help = 'Call cmd command'

    def handle(self, *args, **options):
        # Replace 'your_command' with the command you want to execute
        command = 'CommandApp_USBRelay HURTM open 01'

        try:
            # Execute the command and capture the output
            result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
            output = result.decode('utf-8')
        except subprocess.CalledProcessError as e:
            # If the command returns a non-zero exit status, capture the error output
            output = e.output.decode('utf-8')

        # Print the output to the console
        self.stdout.write(output)

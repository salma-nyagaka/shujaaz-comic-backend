#!/usr/bin/env python3
"""Django's command-line utility for administrative tasks."""
import os
import sys
from django.contrib.sites.models import Site




def main():
    
    sys.path.append('/var/www/vhosts/mysite') 

    new_site = Site.objects.create(domain='ec2-52-66-81-41.ap-south-1.compute.amazonaws.com', name='ec2-52-66-81-41.ap-south-1.compute.amazonaws.com')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shujaaz.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

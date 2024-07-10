#!/usr/bin/env python
"""Utility for managing administrative tasks in Django."""
import os
import sys

def main():
    """Execute administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projectmanagement.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as err:
        raise ImportError(
            "Django couldn't be imported. Ensure it is installed and "
            "available on your PYTHONPATH environment variable. Also, check if "
            "the virtual environment is activated."
        ) from err
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()

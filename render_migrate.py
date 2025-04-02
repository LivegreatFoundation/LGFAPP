#!/usr/bin/env python
import os
import sys
import django
from django.db import connection
from django.conf import settings

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "yourproject.settings")
django.setup()

def run_migrations():
    # First, update any null user_id values in the bookmarks table
    with connection.cursor() as cursor:
        # Get the actual table name (in case you're using table name prefixes)
        table_name = "yourapp_bookmark"  # Replace with your actual table name
        
        # Check if there are any NULL user_id values
        cursor.execute(f"SELECT COUNT(*) FROM {table_name} WHERE user_id IS NULL")
        null_count = cursor.fetchone()[0]
        
        if null_count > 0:
            # Set a default user ID (replace '1' with an appropriate user ID that exists)
            cursor.execute(f"UPDATE {table_name} SET user_id = 1 WHERE user_id IS NULL")
            print(f"Updated {null_count} records with NULL user_id values.")
    
    # Now run the migrations with the --noinput flag
    from django.core.management import call_command
    call_command('migrate', interactive=False)
    print("Migrations completed successfully.")

if __name__ == "__main__":
    run_migrations()
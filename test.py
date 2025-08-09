#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Zero-touch enrollment quickstart sample.

This script forms the quickstart introduction to the zero-touch enrollment
customer API. To learn more, visit https://developer.google.com/zero-touch
"""

import sys
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# OAuth2 scope for Zero-Touch Enrollment API
SCOPES = ['https://www.googleapis.com/auth/androidworkzerotouchemm']
SERVICE_ACCOUNT_KEY_FILE = 'service_account_key.json'

def get_service():
    """Creates an authorized API client service for the zero-touch enrollment API."""
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_KEY_FILE, scopes=SCOPES)
    service = build('androiddeviceprovisioning', 'v1', credentials=credentials)
    return service

def main():
    """Runs the zero-touch enrollment quickstart app."""
    try:
        service = get_service()
        
        # List customers, limit to first customer
        response = service.customers().list(pageSize=1).execute()
        
        if 'customers' not in response or len(response['customers']) == 0:
            print('No zero-touch enrollment account found.')
            sys.exit(1)
        
        customer_account = response['customers'][0]['name']
        
        # List DPCs (device policy controllers) under customer account
        results = service.customers().dpcs().list(parent=customer_account).execute()
        
        for dpc in results.get('dpcs', []):
            dpc_name = dpc.get('dpcName', '-')
            package_name = dpc.get('packageName', '-')
            print(f'Name: {dpc_name}  APK: {package_name}')
    
    except HttpError as e:
        print(f'API error: {e}')
        sys.exit(1)
    except Exception as e:
        print(f'Unexpected error: {e}')
        sys.exit(1)

if __name__ == '__main__':
    main()
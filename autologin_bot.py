import pandas as pd
import requests

# Load credentials from CSV
credentials_df = pd.read_csv('credentials.csv')

# Extract username and password
username = credentials_df['username'][0]
password = credentials_df['password'][0]

# URLs for login
login_url = 'https://example.com/login'
post_login_url = 'https://example.com/login'

# Payload with login credentials
payload = {
    'username': username,
    'password': password
}

# Create a session object to persist cookies
session = requests.Session()

# Send a POST request to login
response = session.post(post_login_url, data=payload)

# Check if login was successful
if response.ok:
    print("Login successful!")
    # Example: Access a protected page
    protected_url = 'https://example.com/protected-page'
    protected_response = session.get(protected_url)
    if protected_response.ok:
        print("Access to protected page successful!")
        print(protected_response.text)  # Print or process the page content
    else:
        print("Failed to access protected page.")
else:
    print("Login failed!")

# Dropbox API Python Project

This is a full-stack Python project that utilizes the Dropbox API (v2) to perform various file operations. The project is built using object-oriented programming principles and includes functionality to upload, list, share, and download files from Dropbox.

## Features

- Upload files to your Dropbox account.
- List all files in your Dropbox account.
- Share files using shared links.
- Download files from your Dropbox account.

## Technologies Used

- Python
- Dropbox API (v2)
- Flask (Python web framework)
- Tailwind CSS (for HTML styling)

## Setup and Installation

1. Clone the repository:
2. Install the required dependencies by running 'pip install dropbox flask'

3. Obtain a Dropbox API access token:

   - Go to the Dropbox Developers website: [https://www.dropbox.com/developers](https://www.dropbox.com/developers)
   - Create a new app and generate an access token with necessary permissions such as:

files.metadata.write,
files.content.write,
files.content.read,
sharing.write,
file_requests.write

4. Configure the access token:

   - Open the `app.py` file and replace `<YOUR_ACCESS_TOKEN>` with your actual Dropbox API access token.

5. Start the application: 'python app.py'

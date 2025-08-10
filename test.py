from google.oauth2 import service_account
from googleapiclient.discovery import build
import requests


def download_file(url, local_filename):
    try:
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(local_filename, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        print(f"File downloaded successfully to {local_filename}")
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error downloading file: {e}")
        return False


SERVICE_ACCOUNT_FILE = "service_account_cred.json"
SCOPES = ["https://www.googleapis.com/auth/drive"]

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)

service = build("drive", "v3", credentials=credentials)

resumefile_dic = (
    service.files()
    .download(
        fileId="1UnaZwlVdjU4gxs4RSECZl6bKo8gx7P0RvL0p7woCjLA",
        mimeType="application/pdf",
    )
    .execute()
)

download_uri = resumefile_dic["response"]["downloadUri"]
print(download_uri)
output_filename = "downloaded_script.pdf"

try:
    download_file(download_uri, output_filename)

except:
    print("error downloading file")

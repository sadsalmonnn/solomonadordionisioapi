from google.oauth2 import service_account
from googleapiclient.discovery import build


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

date_modified = (
    service.files()
    .get(fileId="1UnaZwlVdjU4gxs4RSECZl6bKo8gx7P0RvL0p7woCjLA", fields="modifiedTime")
    .execute()["modifiedTime"]
)

print(date_modified)
print(resumefile_dic)
print("\n")
download_uri = resumefile_dic["response"]["downloadUri"]
print(download_uri)
output_filename = "downloaded_script.pdf"

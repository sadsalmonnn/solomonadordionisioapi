from google.oauth2 import service_account
from googleapiclient.discovery import build


def fetch_and_update_resume():
    try:
        SERVICE_ACCOUNT_FILE = "../service_account_cred.json"
        SCOPES = ["https://www.googleapis.com/auth/drive"]

        credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES
        )

        service = build("drive", "v3", credentials=credentials)

        file_metadata = (
            service.files()
            .get(
                fileId="1UnaZwlVdjU4gxs4RSECZl6bKo8gx7P0RvL0p7woCjLA",
                fields="modifiedTime",
            )
            .execute()
        )
        date_modified = file_metadata.get("modifiedTime")

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

        from .models import Resume

        last_resume = Resume.objects.order_by("-date").first()
        if not last_resume or last_resume.date != date_modified:
            Resume.objects.create(resume_uri=download_uri, date=date_modified)

    except Exception as e:
        print(f"Error fetching resume in ready(): {e}")

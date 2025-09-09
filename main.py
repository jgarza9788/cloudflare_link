import os, sys, subprocess, time, re

DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(DIR)

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os


SCOPES = ["https://www.googleapis.com/auth/documents"]


def get_creds():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
        creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return creds

def overwrite_doc(document_id, new_text):
    creds = get_creds()
    service = build("docs", "v1", credentials=creds)

    # Get current doc length
    doc = service.documents().get(documentId=document_id).execute()
    end_index = doc.get("body")["content"][-1]["endIndex"]

    requests = []
    # Delete everything
    if end_index > 1:
        requests.append({
            "deleteContentRange": {
                "range": {"startIndex": 1, "endIndex": end_index - 1}
            }
        })
    # Insert new text
    requests.append({
        "insertText": {
            "location": {"index": 1},
            "text": new_text
        }
    })

    service.documents().batchUpdate(
        documentId=document_id, body={"requests": requests}
    ).execute()

    print("Document replaced with new text!")

def run_cmd(cmd):
    return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


def main():
    try:
        os.remove('log')
    except FileNotFoundError:
        pass

    # start cloudflared
    proc = run_cmd('cloudflared tunnel --url http://192.168.1.250:5055 --logfile ./log')

    # give it time to start
    time.sleep(10)

    with open('log', 'r') as file:
        nlog = file.read()

    # grab first https:// link
    link = re.findall(r'"message":"\|  https://.*.com', nlog)[0]
    link = link.replace('"message":"|  ',"")
    print(link)

    doc_id = "1cB9W6MXV5T4nBCEowRxvzE6Z3BIQouT2FALJiouczII"
    overwrite_doc(doc_id, f"{link} - this link is good for the day")

    # keep cloudflared alive
    proc.wait()


if __name__ == "__main__":
    main()

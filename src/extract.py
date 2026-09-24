import datetime
import json
import os
import eml_parser
from dotenv import load_dotenv

load_dotenv()
PATH = os.getenv("DATAPATH")
def json_serial(obj):
  if isinstance(obj, datetime.datetime):
      serial = obj.isoformat()
      return serial


with open(f"{PATH}30597185_00_SPICE_.eml", 'rb') as fhdl:
  raw_email = fhdl.read()

ep = eml_parser.EmlParser()
parsed_eml = ep.decode_email_bytes(raw_email)

output_path = 'j.json'
# with open(output_path, "w", encoding="utf-8") as json_file:
#     json.dump(parsed_eml, json_file, default=json_serial, indent=4)

# print(f"Successfully saved parsed JSON output to: {output_path}")
header = parsed_eml.get("header", {})

received = header.get("received", "")
inner_header = header.get("header")

x_apple_action = inner_header.get("x-apple-action")
x_suspected_spam = inner_header.get("x-suspected-spam")
x_spam_flag = inner_header.get("x-spam-flag")
x_apple_movetofolder = inner_header.get("x-apple-movetofolder")
auth_result = inner_header.get("authentication-results","")

subject = header.get("subject", "No Subject")


from_address = header.get("from", "")
to_addresses = header.get("to", [])
date = header.get("date")

# print("--- HEADERS ---")
# print(f"Subject: {subject}")
# print(f"From: {from_address}")
# print(f"To: {to_addresses}")
# print(f"Date: {date}")

print(received)
print(auth_result)
print(x_apple_action)
print(x_spam_flag)
print(x_apple_movetofolder)
print(x_suspected_spam)
# print(json.dumps(parsed_eml, default=json_serial, indent=4))

'''

"x-suspected-spam": [
                "true"
            ],
            "x-mailer": [
                "PHPMailer 6.7 (https://github.com/PHPMailer/PHPMailer)"
            ],
            "to": [
                "robert.b.blevins@icloud.com"
            ],
            "return-path": [
                "<wordpress@testsite01.nabeplog.com>"
            ],
            "x-apple-movetofolder": [
                "Junk "
'''

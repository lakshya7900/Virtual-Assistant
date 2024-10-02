import re
import pandas as pd
import win32com.client
from datetime import datetime, timedelta

outlook = win32com.client.Dispatch('outlook.application')
mapi = outlook.GetNamespace("MAPI")
# inbox = mapi.GetDefaultFolder(6).Folders.Item("AI email testing")
#outlook.GetDefaultFolder(6) .Folders.Item("Your_Folder_Name")
inbox = outlook.GetDefaultFolder(6)
messages = inbox.Items

received_dt = datetime.now() - timedelta(days=1)
received_dt = received_dt.strftime('%m/%d/%Y %H:%M %p')


for message in list(messages):
    #print (message)
    body_content = message.body
    body_content =body_content[body_content.find("Subject:"):]
    #print(body_content)
    figures = re.findall("\d+(?:,\d+)*(?:\.\d+)?",body_content)
    print(figures)
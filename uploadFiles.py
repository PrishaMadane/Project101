import os
import dropbox
from dropbox.files import WriteMode

class TransferData : 
    def __init__ (self, access_token):
        self.access_token= access_token
    
    def upload_file (self, file_from, file_to):
        dbx=dropbox.Dropbox (self.access_token)
    
        for root, dirs, files in os.walk(file_from):

          for filename in files:
            local_path = os.path.join(root, filename)
            relative_path = os.path.relpath(local_path, file_free)
            dropbox_path = os.path.join(file_to,relative_path)
              #upload files
            with open(local_path, 'rb')as f:
                dbx.files.upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main ():
    access_token= 'sl.BIGIKA4vGBNZ5MaiE_qNLB4EgxzYYMT-L0J12F60ZrGeMPVhhAIinZPwnVXg7D16f-nW0E_pZwvy_bb6opt2xDIoQ2apM96ZMDhSS2JRsSTVMHr1l-9JMwpXLHHOJG4Y9YtNHiY'
    transferData= TransferData(access_token)

    file_from = str(input("Enter the file path to transfer : -")) 
    file_to = input("enter the full path to upload to dropbox:- ") 
    # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.

    # API v2 
    transferData.upload_file(file_from, file_to) 
    print("file has been moved !!!")

main()
import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A1WYdURFTLCu84zsUQCjcFjc1hjOg7s9kIEpxylLuS5WfL8m-HblsBjenUUZXnXAjbJUmjjwTZnPcXSAoxMGdmQcOQeQeVhsF-6O0f9ylkMgj3M8tQ5D8bhxDe-uXQw7UDJ2lSj9F_g7'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : -")
    file_to = input("enter the full path to upload to dropbox:- ")  # This is the 
    
  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()
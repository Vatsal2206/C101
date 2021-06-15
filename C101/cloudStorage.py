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
    access_token = 'sl.Ayxj45Hs6wAfYrrMWT4A7tclXJHxeNnqvSyYKK-1kwyd5n4xZ4zyMEropWkdFMitR8BoTp3zYaUotwuSy_jnCo6OQp0p0IOZtb1WXwyR3sjbszKEOQDH-GHkodd_gAcrufvSSslT'
    transferData = TransferData(access_token)

    file_from = "C:/Users/Shashwat Varenya/Desktop/WHjr projects/Visual's Studio Code/PYTHON/C101/testFileFrom.txt"
    file_to = '/Cloud_Storage_/test.txt'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    print('FILE MOVED!!')

main()    
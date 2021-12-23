class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token
        
    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self,access_token)

        with open(file_from,'rb')as f:
            dbx.files_upload(f.read(),file_to)

def main():
    access_token = "sl.A-taCfi1iXtlAvUPOA6e182EptWkJqRYHtvWzDA3g1ZZR1q0kjULRvpz9_Z0090rE1q5Em0zzx0b7KNxVS2fSqTC4oyE51RwDWrQjjLcNPlo32siFF61GrLR24BnfUbGVF_I4so"
    transferData = TransferData(access_token)

    file_from = 'Test.txt'
    file_to = '\Dropbox\Apps\FilesUpload09\Test.txt'

    transferData.upload_file(file_from,file_to)



 
      
     



# This is a sample Python script.
from typing import List, Union

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from fastapi import FastAPI, UploadFile, File
import sys
import hashlib
app = FastAPI()


@app.post("/uploadfiles/{nfc_id}")
async def create_upload_files(
nfc_id: str,
    file0: UploadFile = File(description="File before"),
        file1: UploadFile = File(description="File after")
):

    # Convert files

    file_location_before = nfc_id + '_' + file0.filename
    file_location_after = nfc_id + '_' + file1.filename

    with open(file_location_before, "wb+") as file_object:
        file_object.write(file0.file.read())

    with open(file_location_after, "wb+") as file_object:
        file_object.write(file1.file.read())

    sha1_before = hashlib.sha1()

    with open(file_location_before, 'rb') as f:
        while True:
            data = f.read(65536)
            if not data:
                break
            sha1_before.update(data)

    print(sha1_before.hexdigest())

    sha1_after = hashlib.sha1()

    with open(file_location_after, 'rb') as f:
        while True:
            data = f.read(65536)
            if not data:
                break
            sha1_after.update(data)

    print(sha1_after.hexdigest())

    # Store files



    # create hashes

    # calculate difference
    difference_value = 200

    # return results

    return {'hash_before': sha1_before.hexdigest(),
            'hash_after': sha1_after.hexdigest(),
            'difference': difference_value}
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

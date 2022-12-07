import os
import sys
import shutil
import zipfile

class Zipfile:
    def __init__(self, search_string, fing_replace, filename):
        self.filename = filename
        self.search_string = search_string
        self.find_replace = fing_replace
        self.temp_directory = "unzipped .{}".format(filename)

    def _full_filename(self, filename):
        return os.path.join(self.temp_directory, filename)

    def zip_find_replace(self):
        self.unzip_files()
        self.find_replace()
        self.zip_files()

    def unzip_files(self):
        os.mkdir(self.temp_directory)
        zip = zipfile.Zipfile(self.filename)
        try:
            zip.extractall(self.temp_directory)
        finally:
            zip.close()
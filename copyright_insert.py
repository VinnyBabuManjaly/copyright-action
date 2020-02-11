#
#
# Code to insert copyright to the required files

import os
# import json


class InsertCopyRight:

    def __init__(self):
        try:
            self.data = {}
            # self.data["copyright_string"] = "copyright\n"
            # self.data["path"] = "test"
            # self.data["file_type"] = [".py", ".txt"]

            self.data["copyright_string"] = os.environ["INPUT_COPYRIGHTSTRING"]
            self.data["path"] = os.environ["INPUT_FILEPATH"]
            self.data["file_type"] = os.environ["INPUT_FILETYPE"].split(',')

            # print("copyright_string: ", self.data["copyright_string"])
            # print("path: ", self.data["path"])
            # print("file_type: ", self.data["file_type"])

            # Reading data from config file
            # with open('config.json') as file:
            #     self.data = json.load(file)
        except Exception as e:
            print("Exception in init function: ", e)
        # finally:
            # file.close()

    def listing_files(self):
        try:
            # Getting all the required files from the directory
            files = []
            for _root, _dir, _files in os.walk(self.data["path"]):
                for _filename in _files:
                    # Checking in filename, for file extensions already specified
                    for _length in range(0, len(self.data["file_type"])):
                        if self.data["file_type"][_length] in _filename:
                            # Appending to the list "files", all the files to which copyright have to be merged
                            files.append(os.path.join(_root, _filename))
            return files
        except Exception as e:
            print("Exception in listing_files function: ", e)

    def content_check(self, files):
        try:
            for _file in files:
                # Opening files in Read-Write mode and reading all contents of file to a variable
                file = open(_file, "r+")
                content = file.readlines()

                # Checking if the file is empty and if not empty, whether copyright exist
                if not content:    # When the file is empty
                    print(_file, "is an empty file")

                if content:        # When the file is not empty
                    # Handling multi line copyright
                    if self.copyright_check(content):   # String already present in file
                        print("License string already exists in ", _file)
                    else:                               # String absent in file
                        print("Adding license string as not present in ", _file)
                        self.insert_copyright(content, file)
        except Exception as e:
            print("Exception in content_check function: ", e)
        finally:
            file.close()

    def copyright_check(self, content):
        try:
            # To handle multi line copyright extracting copyright string to a list
            print("copyright_string: ", self.data["copyright_string"])
            copyright_list = self.data["copyright_string"].split('\\n')
            print("copyright_list: ", copyright_list)
            for i in range(0, len(copyright_list) - 1):
                # Comparing copyright with contents line by line, considering number of lines the copyright is spread
                if content[i] == copyright_list[i] + '\n':
                    print("content: ", content[i])
                    _value = True
                else:  # On line where comparison fails, returns False value to content_check function to add copyright
                    return False
            return True  # As all lines of copyright are matching, returns true value, indicating copyright exists
        except Exception as e:
            print("Exception in copyright_check function: ", e)

    def insert_copyright(self, content, file):
        try:
            # Inserting copyright string to the beginning of content variable
            content.insert(0, self.data["copyright_string"])
            # Rewriting contents with copyright to file
            file.seek(0)
            file.writelines(content)
            print("Copyright string added to the file")
        except Exception as e:
            print("Exception in insert_copyright function: ", e)


def main():
    try:
        obj = InsertCopyRight()         # Instantiating object 'obj' for class InsertCopyRight
        files = obj.listing_files()     # Function to get the files into which copyright has to be added
        print("files: ", files)
        if files:
            obj.content_check(files)    # Checking if copyright already exists and if not add respectively
    except Exception as e:
        print("Exception in main function: ", e)


if __name__ == "__main__":
    main()

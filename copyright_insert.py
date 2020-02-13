'''
    File name: copyright_insert.py
    Author: Vinny Babu Manjaly
    Date created: 2/2/2020
    Date last modified: 2/12/2020
    Python Version: 3.7
'''
import os


class InsertCopyRight:

    def __init__(self):
        '''
        Reading input from yaml file in .github/workflows of the working repository
        '''
        try:
            self.data = {}
            self.data['copyright_string'] = os.environ['INPUT_COPYRIGHTSTRING'].replace(
                '\\n', '\n',
            )
            self.data['file_path'] = os.environ['INPUT_FILEPATH'].replace(
                ' ', '',
            ).split(',')
            self.data['file_type'] = os.environ['INPUT_FILETYPE'].replace(
                ' ', '',
            ).split(',')
            self.data['ignore_file_path'] = os.environ['INPUT_IGNOREFILEPATH'].replace(
                ' ', '',
            ).split(',')

            print(
                'ignore_file_path: "',
                os.environ['INPUT_IGNOREFILEPATH'], '"', self.data['ignore_file_path'],
            )
            print('Length: ', len(os.environ['INPUT_IGNOREFILEPATH']))
            print(
                'Length as string: ', len(
                    str(os.environ['INPUT_IGNOREFILEPATH']),
                ),
            )
            if os.environ['INPUT_IGNOREFILEPATH'] is None:
                print('None value')
                self.data['ignore_file_path'] = None
            elif os.environ['INPUT_IGNOREFILEPATH'] == '':
                print('No value in quotes')
            elif os.environ['INPUT_IGNOREFILEPATH'] == ' ':
                print('One space value')
            elif not os.environ['INPUT_IGNOREFILEPATH']:
                print('Not string')
            elif not os.environ['INPUT_IGNOREFILEPATH'].strip():
                print('Empty String!')

        except Exception as e:
            print('Exception in init function: ', e)

    def listing_files(self):
        '''
        Getting all the required files from the directory
        Checking in filename, for file extensions already specified
        Appending to the list "files", all the files to which copyright have to be merged
        :return:
        '''
        try:
            files = []
            _value = False
            for _path in self.data['file_path']:
                for _root, _dir, _files in os.walk(_path):
                    if self.data['ignore_file_path'] is not None:
                        for _ignore_path in self.data['ignore_file_path']:
                            if _ignore_path not in _root:
                                _value = False
                            else:
                                print('Ignoring file path ', _root)
                                _value = True
                                break
                    if _value is False:
                        for _filename in _files:
                            for file_type in self.data['file_type']:
                                if file_type in _filename:
                                    files.append(
                                        os.path.join(_root, _filename),
                                    )
            return files
        except Exception as e:
            print('Exception in listing_files function: ', e)

    def content_check(self, files):
        '''
        Opening files in Read-Write mode and reading all contents of file to a variable
        Checking if the file is empty and if not empty, whether copyright exists
        When the file is empty, not writing the copyright string to the file
        When the file is not empty, handling multi line copyright and checking whether its present in the file
        :param files:
        :return:
        '''
        try:
            for _file in files:
                file = open(_file, 'r+', errors='ignore')
                content = file.readlines()
                if not content:
                    print(
                        _file, 'is an empty file, hence not adding the copyright or license to the file',
                    )
                if content:
                    if self.copyright_check(content):
                        print('License string already exists in ', _file)
                    else:
                        print('Adding license string as not present in ', _file)
                        self.insert_copyright(content, file)
        except Exception as e:
            print('Exception in content_check function: ', e)
        finally:
            file.close()

    def copyright_check(self, content):
        '''
        To handle multi line copyright extracting copyright string to a list
        Comparing copyright with contents line by line, considering number of lines the copyright is spread
        On line where comparison fails, returns False value to content_check function to add copyright
        As all lines of copyright are matching, returns true value, indicating copyright exists
        :param content:
        :return:
        '''
        try:
            copyright_list = self.data['copyright_string'].split('\n')
            for i in range(0, len(copyright_list) - 1):
                if content[i] == copyright_list[i] + '\n':
                    _value = True
                else:
                    return False
            return True
        except Exception as e:
            print('Exception in copyright_check function: ', e)

    def insert_copyright(self, content, file):
        '''
        Inserting copyright string to the beginning of content variable
        Rewriting contents with copyright to file
        '''
        try:
            content.insert(0, self.data['copyright_string'])
            file.seek(0)
            file.writelines(content)
        except Exception as e:
            print('Exception in insert_copyright function: ', e)


def main():
    '''
    Instantiating object 'obj' for class InsertCopyRight
    Function to get the files into which copyright has to be added
    Checking if copyright already exists and if not add respectively
    '''
    try:
        obj = InsertCopyRight()
        files = obj.listing_files()
        print('List of files to be checked for copyright notice:\n', files)
        if files:
            obj.content_check(files)
    except Exception as e:
        print('Exception in main function: ', e)


if __name__ == '__main__':
    main()

import os
import platform
import re
import zipfile

examples_folder_path = {
    'DESKTOP-62BVD4A': 'C:\\Users\\User\\PycharmProjects\\EPUB_to_HTML_converter\\Examples',
    'hellerick-C17A': r'/home/hellerick/PycharmProjects/PUB_to_HTML_converter/Examples'}[platform.node()]

epub_path = os.path.join(examples_folder_path, 'Ginei_01_EN.epub')

def unzip(epub_path):
    print(f'Unzipping the file \n{epub_path}\n')
    folder_path, epub_filename = os.path.split(epub_path)
    epub_file = zipfile.ZipFile(epub_path)
    contents_folder_name = re.sub(r'(\.epub)?\Z', '.contents', epub_filename)
    contents_folder_path = os.path.join(folder_path, contents_folder_name)
    for subpath in epub_file.namelist():
        subfolder_name, subfile_name = os.path.split(subpath)
        full_subfolder_path = os.path.join(contents_folder_path, subfolder_name)
        if not os.path.exists(full_subfolder_path):
            os.makedirs(full_subfolder_path)
        print(f'Extracting file {subfile_name} at: {full_subfolder_path}')
        epub_file.extract(subpath, contents_folder_path)
        # epub_file.extract(subfile)
        # epub_file.extract
        # if f.endswith('/'):
        #     pass
            # os.makedirs(f)

def convert_epub_to_html(epub_path):
    print(f'Processing the file \n{epub_path}\n')
    folder_path, epub_filename = os.path.split(epub_path)
    # print('Folder', folder_path, 'File', epub_filename)
    unzip(epub_path)

    # content.opf # spine -- default reading order

if __name__ == '__main__':
    convert_epub_to_html(epub_path)
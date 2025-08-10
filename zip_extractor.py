import zipfile
import pathlib

def extract_archive(zipfilepath, dest_dir):
    zipfilepath = pathlib.Path(zipfilepath)
    dest_dir = pathlib.Path(dest_dir)
    with zipfile.ZipFile(zipfilepath ,'r') as zipfileptr:
        zipfileptr.extractall(dest_dir)
    return 'Success'


if __name__ == '__main__':
    extract_archive(r"C:\m18_work\udemy\ThePythonMegaCourse\old_arch\cmp\compressed.zip", 
                    r"C:\m18_work\udemy\ThePythonMegaCourse\old_arch\cmp")
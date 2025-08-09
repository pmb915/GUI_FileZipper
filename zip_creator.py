
import zipfile
import pathlib

def make_archive(filepaths, dest_folder):
    dest_path = pathlib.Path(dest_folder, "compressed.zip")
    with zipfile.ZipFile(dest_path, "w") as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname= filepath.name)
    return 'Compression completed!'


if __name__ == "__main__":
    filelist = ['C:/m18_work/udemy/ThePythonMegaCourse/old_arch/file1.txt', 'C:/m18_work/udemy/ThePythonMegaCourse/old_arch/file3.txt']
    arch_loc =  "C:/m18_work/udemy/ThePythonMegaCourse/old_arch/cmp"
    #arch_loc= pathlib.Path(arch_loc, "compressed.zip")
    x=make_archive(filelist, arch_loc)
    print(x)

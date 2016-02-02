import os


# remove numbers in the filenames of all the files in a folder
def rename_files():

    # Get filenames from a given folder
    file_list = os.listdir(r"/Users/path_to_file/prank")
    print (file_list)
    saved_path = os.getcwd()
    print (saved_path)
    os.chdir(r"/Users/path_to_file/prank")

    # for each file, rename the file name
    for file_name in file_list:
        print ("old_name " + file_name)
        print ("New_name " + file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))
    print (file_list)
    os.chdir(saved_path)

rename_files()
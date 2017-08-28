import os

root = "/home/vanessa/prank"
def rename_files():
    file_list = os.listdir("/home/vanessa/prank")
    for file_name in file_list:
        os.rename(os.path.join(root, file_name),
                  os.path.join(root, file_name.translate(None, "0,1,2,3,4,5,6,7,8,9")))
    rename_files()

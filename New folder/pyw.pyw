from imp import source_from_cache
import os
import shutil
from os import path




def main():
    if path.exists("C:/Users/mrvsv/OneDrive/coding/copy.txt"):
      src=path.realpath("C:/Users/mrvsv/OneDrive/coding/copy.txt")
    source="C:/Users/mrvsv/OneDrive/coding/copy.txt"
    rename="C:/Users/mrvsv/OneDrive/coding/main.txt"
    os.rename(source,rename)
    print("Successfully renamed")
if __name__=="__main__":
    main()








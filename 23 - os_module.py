import os

print(os.getcwd())      # It prints the directory which we are currently working on
#print(os.chdir())      # We need to pass the path to which we want to change the directory
print(os.listdir())     # It prints the list of files or directories that are present are in the current working directory

# os.mkdir()            # Pass the directory name we want to create in the current directory

# os.rmdir              # It removes the file being specified in the current directory

# os.removedirs         # it is also the same as the rmdir method

# os.rename()           # It renmaes the file being specified 
# print(os.stat(filename))      # It gives some information about the file

'''we get the some information about the file using the stat method but we can't understand the variables being used
we can get the siez of the file usng the ".st_size" we add it to the stat method  in the same way the time we modified the
file can also get using the human readable form using the datetime module'''

from datetime import datetime

modified_time = os.stat('cyberbullying_tweets.csv').st_mtime

print(datetime.fromtimestamp(modified_time))      


'''If we want to see all the tree directiroes within the os module ten we use the "os.walk()" where it takes
three arguements i) the directories path, ii) directories within that path  iii) files within that path'''
#print(os.walk())  

'''for dir_path, dirs, files in os.walk(os.getcwd):
    print("current directiory path:", dir_path)
    print("Current Directory:", dirs)
    print("Current File:",files)'''
    
# os.path.join(filepath, file)      # It helps us to join the file to th mentioned file location
# os.path.basename(filepath)        # It helps us in providing the actual filename 
# os.path.dirname(filepath)         # It hepls us in printing the directory name
# os.path.split(filepath)           # It hepls us in printing the directory and file name separately
# os.path.exists(filepath)          # It returns a boolean value checks whether the file exists or  not
# os.path.isdir(filepath)           # Checks whether it is a directory or not
# os.path.isfile(filepath)          # Checks whether it is a file or not 
# os.path.splitext(filepath)        # It divides the file and the root extensionof the file   
      
 
import subprocess
import os
import re

output = []
num = 1
# create a list of folders nees to scrape through
os.chdir('1.設計影像總管/2.理論分類')
process = subprocess.Popen(["ls"], stdout=subprocess.PIPE)
folders = process.communicate()[0].decode('utf-8')
folders = folders.splitlines()

# scrape through all the folders for all their subfolders name
for i, folder in enumerate(folders):
    # go inside folders
    os.chdir(folder)
    
    # fetch the name of all the subfolders  
    subfolders = [ name for name in os.listdir() if os.path.isdir(name) ]
    #process = subprocess.Popen(["ls"], stdout=subprocess.PIPE)
    #subfolders = process.communicate()[0].decode('utf-8')
    #subfolders = subfolders.splitlines()
            
    # produce the correct output for comment
    stdout = subfolders
    stdout = [re.sub(r'(^.+)\.', '', str(c)) for c in stdout]  # rip off all characters before .
    stdout = [c + f' ({c[:3].lower()})' for c in stdout]  # add three words acronym to the end of string
    
    for j, c in enumerate(stdout):
        # for comment
        #s = f'# B{i+1}{chr(97+j)}-' + c
        
        # for enum class code
        s = f' B{i+1}{chr(97+j)} = {num}'
        num += 1
        output.append(s)
    
    os.chdir('..')

print('; '.join(output))
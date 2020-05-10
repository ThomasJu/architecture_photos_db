from pathlib import Path
import extract_date as ed
import category_class as cc

# lambda that deletes dot
no_dot_func = lambda s : s[s.find('.')+1:]

# create a sample from all path in the folders
p = Path('.')
all_jpg_path = list(p.glob('**/*.jpg'))
sample = all_jpg_path[15]
print(sample)

# extract all column features from a sample picture
sample_path = list(map(no_dot_func, list(sample.parts)[1:-1]))
sample_date = ed.extract_date(sample.name)

print(cc.categorydict[0][sample_path[0]])
print(cc.categorydict[1][sample_path[1]])

print(sample_path)
print(sample_date)

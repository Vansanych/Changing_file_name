import os

# dir_name = r'C:\Users\User\Desktop\Логачев\ТК формат разработки'
files = os.listdir(dir_name)


for i in range(7, 58):
    os.rename(dir_name + '\\' + files[i], dir_name + '\\' + str(files[i].replace('001-08-2020', '-2022_ГСП_СИК_КР.1279 – 1307,8')))

import os
import random
import configparser

def config_cc(path):
    wallpaper_database = os.listdir(path)
    wallpaper_database_length = len(wallpaper_database)
    print(wallpaper_database_length)
    config = configparser.ConfigParser()
    config['settings'] = {'path': path, 'cfg_ver': 'indev_25_12_Getsu_08_04a20', 'wallpaper_database': wallpaper_database_length}
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
        
def config_cc_form():
        usrdir = input("Type full path to directory(leave empty if you are already in desired directory):")
        if usrdir == "":
            usrdir = os.getcwd()
            config_cc(usrdir)
        else:
            config_cc(usrdir)

def read_conf():
    config = configparser.ConfigParser()
    config.read('config.ini')
    path = config.get('settings', 'path')
    dir_size = config.get('settings', 'wallpaper_database')
    config_dic = {
        'path': path,
        'wallpaper_database': dir_size
    }
    return config_dic

#Main algorithm
def wallpaper_choose():
    conf = read_conf()
    wallpaper_database_length = conf['wallpaper_database']
    wallpaper_database_length = int(wallpaper_database_length)
    random_num_wallpaper = random.randint(0, wallpaper_database_length)
    path = conf['path']
    print(random_num_wallpaper)
    dir = os.listdir(path)
    random_wallpaper = dir[random_num_wallpaper]
    os.system(f'feh --bg-scale "{path}{random_wallpaper}"')

listdir = os.listdir()
if 'config.ini' in listdir:
    wallpaper_choose()
else:
    config_cc_form()

    
